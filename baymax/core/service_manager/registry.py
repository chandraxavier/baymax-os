"""
Service registry for Baymax OS.
"""

from __future__ import annotations

from baymax.interfaces.service import BaymaxService


class ServiceRegistry:
    """Stores service instances registered with the Runtime Engine."""

    def __init__(self) -> None:
        self._services: dict[str, BaymaxService] = {}

    def register(self, service: BaymaxService) -> None:
        """Register a service instance."""

        if service.name in self._services:
            raise ValueError(f"Service already registered: {service.name}")

        self._services[service.name] = service

    def get(self, service_name: str) -> BaymaxService:
        """Return a registered service by name."""

        try:
            return self._services[service_name]
        except KeyError as exc:
            raise KeyError(f"Unknown service: {service_name}") from exc

    def all(self) -> tuple[BaymaxService, ...]:
        """Return all registered services."""

        return tuple(self._services.values())

    def names(self) -> tuple[str, ...]:
        """Return registered service names."""

        return tuple(self._services)
