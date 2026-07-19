"""
Baymax Device Runtime Service.
"""

from __future__ import annotations

from typing import Sequence

from baymax.core.health import HealthStatus
from baymax.interfaces.service import BaymaxService
from baymax.services.device.manager import DeviceManager
from baymax.services.device.probes.audio import AudioProbe


class DeviceRuntime(BaymaxService):
    @property
    def name(self) -> str:
        return "device"

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def dependencies(self) -> Sequence[str]:
        return ()

    def __init__(self, context):
        super().__init__(context)
        self._manager = DeviceManager()

    async def initialize(self) -> None:
        self._manager.register_probe(AudioProbe())

    async def start(self) -> None:
        devices = self._manager.discover()

        self.context.logger.info(
            "device_manager_started",
            devices=len(devices),
        )

    async def stop(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass

    async def health(self) -> dict:
        devices = self._manager.discover()

        return {
            "service": self.name,
            "status": HealthStatus.HEALTHY.value,
            "devices": len(devices),
        }

    async def status(self) -> dict:
        return {
            "devices": self._manager.discover(),
        }
