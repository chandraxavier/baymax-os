"""
Baymax OS Runtime Engine.
"""

from __future__ import annotations

import logging
from pathlib import Path

from baymax.core.configuration.manager import ConfigurationManager
from baymax.core.logging import configure_logging
from baymax.core.runtime.context import RuntimeContext
from baymax.core.runtime.lifecycle import RuntimeLifecycle
from baymax.core.runtime.state import RuntimeState


class RuntimeEngine:
    """
    Boot and shutdown coordinator for Baymax OS.

    The Runtime Engine owns core managers and creates the immutable
    ``RuntimeContext`` passed into platform services.
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
        self._context: RuntimeContext | None = None
        self._logger = logging.getLogger("baymax.runtime")

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

    def boot(self) -> RuntimeContext:
        """
        Boot Baymax OS core infrastructure.

        The current Sprint 1 boot path initializes configuration, logging, and
        runtime context. Service registration and start order will be layered
        on top of this engine through the Service Manager.
        """

        self._transition(RuntimeState.BOOTING)

        try:
            self._transition(RuntimeState.CONFIGURING)
            self._configuration_manager.load()
            configuration = self._configuration_manager.configuration

            log_directory = Path(configuration.logging.directory)
            self._logger = configure_logging(
                level=configuration.logging.level,
                log_directory=log_directory,
            ).getChild("runtime")

            self._transition(RuntimeState.INITIALIZING)
            self._context = RuntimeContext(
                platform_version=(
                    configuration.system.version or self._platform_version
                ),
                development_mode=configuration.system.development_mode,
                configuration=self._configuration_manager,
                logger=self._logger,
            )

            self._transition(RuntimeState.RUNNING)
            self._logger.info(
                "Runtime boot completed.",
                extra={"baymax_service": "runtime"},
            )
            return self._context
        except Exception:
            self._transition(RuntimeState.FAILED)
            self._logger.exception(
                "Runtime boot failed.",
                extra={"baymax_service": "runtime"},
            )
            raise

    def shutdown(self) -> None:
        """Shutdown Baymax OS core infrastructure."""

        if self.state is RuntimeState.STOPPED:
            return

        self._transition(RuntimeState.STOPPING)
        self._logger.info(
            "Runtime shutdown completed.",
            extra={"baymax_service": "runtime"},
        )
        self._transition(RuntimeState.STOPPED)

    def _transition(self, new_state: RuntimeState) -> None:
        """Apply and log a runtime lifecycle transition."""

        previous_state = self.state
        self._lifecycle.transition_to(new_state)

        if self._logger.handlers or self._logger.parent:
            self._logger.info(
                "Runtime state transition: "
                f"{previous_state.value} -> {new_state.value}.",
                extra={"baymax_service": "runtime"},
                stacklevel=2,
            )
