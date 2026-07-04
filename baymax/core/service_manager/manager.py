"""
Baymax OS service manager.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from baymax.core.eventbus import Event, EventBus, EventTopic
from baymax.core.health import HealthManager, HealthReport, HealthStatus
from baymax.core.service_manager.models import (
    SERVICE_STATE_TRANSITIONS,
    ServiceState,
    ServiceStatus,
)
from baymax.core.service_manager.registry import ServiceRegistry
from baymax.interfaces.service import BaymaxService


class ServiceDependencyError(RuntimeError):
    """Raised when service dependencies cannot be resolved."""


class ServiceLifecycleError(RuntimeError):
    """Raised when a service lifecycle transition is invalid."""


class ServiceManager:
    """
    Owns registration and lifecycle management for Baymax services.

    Services declare dependencies, but only the manager initializes, starts,
    stops, restarts, and queries services.
    """

    def __init__(
        self,
        registry: ServiceRegistry,
        events: EventBus,
        health: HealthManager,
        logger: Any,
    ) -> None:
        self._registry = registry
        self._events = events
        self._health = health
        self._logger = logger
        self._states: dict[str, ServiceState] = {}

    @property
    def registry(self) -> ServiceRegistry:
        """Registered service registry."""

        return self._registry

    def register(self, service: BaymaxService) -> None:
        """Register a service for lifecycle management."""

        self._registry.register(service)
        self._states[service.name] = ServiceState.CREATED
        self._logger.info(
            "service_registered",
            service=service.name,
            version=service.version,
        )

    async def start_all(self) -> None:
        """Initialize and start all services in dependency order."""

        for service in self._dependency_order():
            await self.start(service.name)

    async def stop_all(self) -> None:
        """Stop all running services in reverse dependency order."""

        for service in reversed(self._dependency_order()):
            await self.stop(service.name)

    async def start(self, service_name: str) -> None:
        """Initialize and start a registered service."""

        service = self._registry.get(service_name)
        state = self._states[service.name]

        if state is ServiceState.RUNNING:
            return

        if state is ServiceState.CREATED:
            await service.initialize()
            self._transition(service, ServiceState.INITIALIZED)
            await self._publish(
                EventTopic.SERVICE_INITIALIZED,
                service,
                {"state": ServiceState.INITIALIZED.value},
            )

        self._transition(service, ServiceState.STARTING)
        await service.start()
        self._transition(service, ServiceState.RUNNING)
        await self._publish(
            EventTopic.SERVICE_STARTED,
            service,
            {"state": ServiceState.RUNNING.value},
        )
        await self.collect_health(service.name)

    async def stop(self, service_name: str) -> None:
        """Stop a registered service if it is active."""

        service = self._registry.get(service_name)
        state = self._states[service.name]

        if state in {ServiceState.CREATED, ServiceState.STOPPED}:
            return

        self._transition(service, ServiceState.STOPPING)
        await service.stop()
        await service.shutdown()
        self._transition(service, ServiceState.STOPPED)
        await self._publish(
            EventTopic.SERVICE_STOPPED,
            service,
            {"state": ServiceState.STOPPED.value},
        )

    async def restart(self, service_name: str) -> None:
        """Restart a registered service."""

        await self.stop(service_name)
        await self.start(service_name)

    async def collect_health(
        self,
        service_name: str | None = None,
    ) -> tuple[HealthReport, ...]:
        """Collect health reports from one service or all services."""

        services = (
            (self._registry.get(service_name),)
            if service_name is not None
            else self._registry.all()
        )
        reports: list[HealthReport] = []

        for service in services:
            payload = await service.health()
            report = HealthReport(
                service=service.name,
                status=HealthStatus(payload["status"]),
                message=payload.get("message", ""),
                version=service.version,
                uptime_seconds=int(payload.get("uptime_seconds", 0)),
                details=payload.get("details", {}),
            )
            self._health.record(report)
            reports.append(report)
            await self._events.publish(
                Event(
                    topic=EventTopic.HEALTH_UPDATED.value,
                    source="service-manager",
                    payload=report.as_dict(),
                )
            )

        return tuple(reports)

    def status(self, service_name: str) -> ServiceStatus:
        """Return status for a registered service."""

        service = self._registry.get(service_name)
        return ServiceStatus(
            name=service.name,
            version=service.version,
            state=self._states[service.name],
            dependencies=tuple(service.dependencies),
        )

    def statuses(self) -> tuple[ServiceStatus, ...]:
        """Return statuses for all registered services."""

        return tuple(self.status(service.name) for service in self._registry.all())

    def _dependency_order(self) -> tuple[BaymaxService, ...]:
        """Return services in dependency-safe startup order."""

        ordered: list[BaymaxService] = []
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(service: BaymaxService) -> None:
            if service.name in visited:
                return

            if service.name in visiting:
                raise ServiceDependencyError(
                    f"Circular service dependency at {service.name}."
                )

            visiting.add(service.name)

            for dependency in service.dependencies:
                visit(self._registry.get(dependency))

            visiting.remove(service.name)
            visited.add(service.name)
            ordered.append(service)

        for registered_service in self._registry.all():
            visit(registered_service)

        return tuple(ordered)

    def _transition(
        self,
        service: BaymaxService,
        new_state: ServiceState,
    ) -> None:
        """Apply a validated service lifecycle transition."""

        previous_state = self._states[service.name]
        allowed_states = SERVICE_STATE_TRANSITIONS[previous_state]

        if new_state not in allowed_states:
            raise ServiceLifecycleError(
                "Invalid service transition "
                f"{service.name}: {previous_state.value} -> "
                f"{new_state.value}."
            )

        self._states[service.name] = new_state
        self._logger.info(
            "service_state_changed",
            service=service.name,
            previous_state=previous_state.value,
            new_state=new_state.value,
            changed_at=datetime.now(timezone.utc).isoformat(),
        )

    async def _publish(
        self,
        topic: EventTopic,
        service: BaymaxService,
        payload: dict[str, Any],
    ) -> None:
        """Publish a service lifecycle event."""

        await self._events.publish(
            Event(
                topic=topic.value,
                source="service-manager",
                payload={"service": service.name, **payload},
            )
        )
