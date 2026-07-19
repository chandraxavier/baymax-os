"""
Baymax Vehicle Runtime Service.
"""

from __future__ import annotations

from typing import Sequence

from baymax.core.health import HealthStatus
from baymax.interfaces.service import BaymaxService
from baymax.services.vehicle.manager import VehicleManager


class VehicleRuntime(BaymaxService):
    @property
    def name(self) -> str:
        return "vehicle"

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def dependencies(self) -> Sequence[str]:
        return ("device",)

    def __init__(self, context):
        super().__init__(context)
        self._manager = VehicleManager()

    async def initialize(self) -> None:
        pass

    async def start(self) -> None:
        self.context.logger.info(
            "vehicle_runtime_started",
            state=self._manager.state.value,
        )

    async def stop(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass

    async def health(self) -> dict:
        return {
            "service": self.name,
            "status": HealthStatus.HEALTHY.value,
            "state": self._manager.state.value,
        }

    async def status(self) -> dict:
        return {
            "state": self._manager.state.value,
            "telemetry": self._manager.telemetry,
        }
