"""
Baymax Voice Runtime Service.
"""

from __future__ import annotations

from typing import Sequence

from baymax.core.health import HealthStatus
from baymax.interfaces.service import BaymaxService
from baymax.services.voice.manager import VoiceManager


class VoiceRuntime(BaymaxService):
    @property
    def name(self) -> str:
        return "voice"

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def dependencies(self) -> Sequence[str]:
        return ("guardian", "audio")

    def __init__(self, context):
        super().__init__(context)
        self._manager = VoiceManager(context)

    async def initialize(self) -> None:
        pass

    async def start(self) -> None:
        self.context.logger.info("voice_started")

    async def stop(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass

    async def health(self) -> dict:
        return {
            "service": self.name,
            "status": HealthStatus.HEALTHY.value,
        }

    async def process(self, text: str) -> dict:
        return await self._manager.process(text)

    async def status(self) -> dict:
        return {
            "service": self.name,
            "ready": True,
        }
