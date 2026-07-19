"""
Baymax Audio Runtime Service.
"""

from __future__ import annotations

from typing import Sequence

from baymax.core.health import HealthStatus
from baymax.interfaces.service import BaymaxService
from baymax.services.audio.manager import AudioManager


class AudioRuntime(BaymaxService):
    @property
    def name(self) -> str:
        return "audio"

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def dependencies(self) -> Sequence[str]:
        return ("guardian",)

    def __init__(self, context):
        super().__init__(context)
        self._manager = AudioManager()

    async def initialize(self) -> None:
        pass

    async def start(self) -> None:
        self.context.logger.info(
            "audio_started",
            outputs=len(self._manager.list_outputs()),
        )

    async def stop(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass

    async def health(self) -> dict:
        outputs = self._manager.list_outputs()

        return {
            "service": self.name,
            "status": HealthStatus.HEALTHY.value if outputs else HealthStatus.DEGRADED.value,
            "outputs": len(outputs),
        }

    async def status(self) -> dict:
        return {
            "service": self.name,
            "outputs": self._manager.list_outputs(),
        }
