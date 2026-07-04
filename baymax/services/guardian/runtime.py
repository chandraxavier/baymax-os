"""
Baymax Guardian service.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Sequence

import psutil

from baymax.core.eventbus import Event, EventTopic
from baymax.core.health import HealthStatus
from baymax.interfaces.service import BaymaxService
from baymax.services.guardian.state_machine import GuardianState


class GuardianRuntime(BaymaxService):
    """
    Operating system supervisor for Baymax OS.

    Guardian starts after core runtime infrastructure is ready. It observes
    runtime state through injected dependencies and publishes lifecycle events.
    """

    @property
    def name(self) -> str:
        """Unique service name."""

        return "guardian"

    @property
    def version(self) -> str:
        """Guardian service version."""

        return "0.1.0"

    @property
    def dependencies(self) -> Sequence[str]:
        """Services required before Guardian starts."""

        return ()

    def __init__(self, context) -> None:
        super().__init__(context)
        self._state = GuardianState.BOOTING
        self._started_at: datetime | None = None

    async def initialize(self) -> None:
        """Initialize Guardian supervision state."""

        self._transition(GuardianState.INITIALIZING)

    async def start(self) -> None:
        """Start Guardian supervision."""

        self._started_at = datetime.now(timezone.utc)
        self._transition(GuardianState.RUNNING)

        if self.context.events is not None:
            await self.context.events.publish(
                Event(
                    topic=EventTopic.GUARDIAN_READY.value,
                    source=self.name,
                    payload={"state": self._state.value},
                )
            )

    async def stop(self) -> None:
        """Stop Guardian supervision."""

        self._transition(GuardianState.SHUTTING_DOWN)

    async def shutdown(self) -> None:
        """Release Guardian resources."""

        self._transition(GuardianState.POWER_OFF)

    async def health(self) -> dict:
        """Return Guardian health and platform telemetry."""

        uptime_seconds = 0
        if self._started_at is not None:
            uptime_seconds = int(
                (datetime.now(timezone.utc) - self._started_at).total_seconds()
            )

        return {
            "service": self.name,
            "status": HealthStatus.HEALTHY.value,
            "message": "Guardian supervision is running.",
            "uptime_seconds": uptime_seconds,
            "details": {
                "state": self._state.value,
                "cpu_percent": psutil.cpu_percent(interval=None),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage("/").percent,
            },
        }

    async def status(self) -> dict:
        """Return Guardian lifecycle status."""

        return {
            "service": self.name,
            "version": self.version,
            "state": self._state.value,
            "dependencies": list(self.dependencies),
        }

    def _transition(self, new_state: GuardianState) -> None:
        """Apply a Guardian state transition."""

        previous_state = self._state
        self._state = new_state

        if self.context.logger is not None:
            self.context.logger.info(
                "guardian_state_changed",
                service=self.name,
                previous_state=previous_state.value,
                new_state=new_state.value,
            )


if __name__ == "__main__":
    raise SystemExit(
        "GuardianRuntime is started by baymax.core.runtime.engine."
    )
