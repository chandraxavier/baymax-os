"""
Baymax OS Runtime Engine.
"""

from __future__ import annotations

import asyncio
from pathlib import Path

from baymax.core.configuration.manager import ConfigurationManager
from baymax.core.eventbus import Event, EventBus, EventTopic
from baymax.core.health import HealthManager
from baymax.core.logging import configure_logging, get_logger
from baymax.core.runtime.context import RuntimeContext
from baymax.core.runtime.lifecycle import RuntimeLifecycle
from baymax.core.runtime.state import RuntimeState
from baymax.core.service_manager import ServiceManager, ServiceRegistry
from baymax.services.guardian.runtime import GuardianRuntime


class RuntimeEngine:
    """
    Boot and shutdown coordinator for Baymax OS.

    The Runtime Engine owns core managers, creates the immutable
    ``RuntimeContext``, registers core services, and starts managed services
    through the Service Manager.
    """

    def __init__(
        self,
        config_root: Path,
        platform_version: str = "0.1.0",
    ) -> None:
        self._config_root = config_root
        self._platform_version = platform_version
        self._lifecycle = RuntimeLifecycle()
        self._configuration_manager = ConfigurationManager(config_root)
        self._events = EventBus()
        self._registry = ServiceRegistry()
        self._health = HealthManager()
        self._service_manager: ServiceManager | None = None
        self._context: RuntimeContext | None = None
        self._logger = get_logger("baymax.runtime")

    @property
    def state(self) -> RuntimeState:
        """Current runtime state."""

        return self._lifecycle.state

    @property
    def context(self) -> RuntimeContext:
        """Return the initialized runtime context."""

        if self._context is None:
            raise RuntimeError("Runtime context is not initialized.")

        return self._context

    @property
    def lifecycle(self) -> RuntimeLifecycle:
        """Runtime lifecycle controller."""

        return self._lifecycle

    @property
    def service_manager(self) -> ServiceManager:
        """Return the initialized service manager."""

        if self._service_manager is None:
            raise RuntimeError("Service manager is not initialized.")

        return self._service_manager

    def boot(self) -> RuntimeContext:
        """Synchronously boot Baymax OS core infrastructure."""

        return asyncio.run(self.boot_async())

    async def boot_async(self) -> RuntimeContext:
        """
        Boot Baymax OS core infrastructure and core services.

        Boot order:

        1. Load configuration.
        2. Initialize structured logging.
        3. Create runtime context.
        4. Create service manager.
        5. Register core services.
        6. Start Guardian.
        7. Publish runtime ready.
        """

        self._transition(RuntimeState.BOOTING)

        try:
            self._transition(RuntimeState.CONFIGURING)
            self._configuration_manager.load()
            configuration = self._configuration_manager.configuration

            self._logger = configure_logging(
                level=configuration.logging.level,
                log_directory=Path(configuration.logging.directory),
                json_logging=configuration.logging.json_logging,
            ).bind(component="runtime")
            self._logger.info("baymax_runtime")
            self._logger.info("configuration_loaded")
            self._logger.info("logger_ready")

            self._transition(RuntimeState.INITIALIZING)
            self._context = RuntimeContext(
                platform_version=(
                    configuration.system.version or self._platform_version
                ),
                development_mode=configuration.system.development_mode,
                configuration=self._configuration_manager,
                logger=self._logger,
                events=self._events,
                registry=self._registry,
                health=self._health,
            )
            self._logger.info("runtime_context_ready")

            self._service_manager = ServiceManager(
                registry=self._registry,
                events=self._events,
                health=self._health,
                logger=self._logger.bind(component="service-manager"),
            )
            object.__setattr__(
                self._context,
                "service_manager",
                self._service_manager,
            )
            self._logger.info("service_manager_ready")

            self._register_core_services()
            await self._service_manager.start_all()
            self._logger.info("guardian_ready")

            await self._service_manager.collect_health()
            self._logger.info("event_bus_ready")
            self._logger.info("health_manager_ready")

            self._transition(RuntimeState.RUNNING)
            await self._events.publish(
                Event(
                    topic=EventTopic.RUNTIME_READY.value,
                    source="runtime",
                    payload={"state": self.state.value},
                )
            )
            self._logger.info("runtime_ready")
            return self._context
        except Exception:
            self._transition(RuntimeState.FAILED)
            self._logger.exception("runtime_boot_failed")
            raise

    def shutdown(self) -> None:
        """Synchronously shutdown Baymax OS core infrastructure."""

        asyncio.run(self.shutdown_async())

    async def shutdown_async(self) -> None:
        """Shutdown Baymax OS core services and infrastructure."""

        if self.state is RuntimeState.STOPPED:
            return

        if self._service_manager is not None:
            await self._events.publish(
                Event(
                    topic=EventTopic.RUNTIME_STOPPING.value,
                    source="runtime",
                    payload={"state": RuntimeState.STOPPING.value},
                )
            )

        self._transition(RuntimeState.STOPPING)

        if self._service_manager is not None:
            await self._service_manager.stop_all()

        self._transition(RuntimeState.STOPPED)
        self._logger.info("runtime_stopped")

    def _register_core_services(self) -> None:
        """Register core services owned by the Runtime Engine."""

        self.service_manager.register(GuardianRuntime(self.context))

    def _transition(self, new_state: RuntimeState) -> None:
        """Apply and log a runtime lifecycle transition."""

        previous_state = self.state
        self._lifecycle.transition_to(new_state)
        self._logger.info(
            "runtime_state_changed",
            previous_state=previous_state.value,
            new_state=new_state.value,
        )

def main() -> int:
    """Run the Baymax Runtime."""

    import time

    engine = RuntimeEngine(config_root=Path("config"))

    try:
        engine.boot()

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        pass

    finally:
        engine.shutdown()

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
