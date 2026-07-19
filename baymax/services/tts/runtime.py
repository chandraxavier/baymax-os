"""
Baymax Text To Speech Runtime Service.
"""

from __future__ import annotations

from typing import Sequence

from baymax.core.health import HealthStatus
from baymax.interfaces.service import BaymaxService
from baymax.services.tts.engine import TTSFactory


class TTSRuntime(BaymaxService):

    @property
    def name(self) -> str:
        return "tts"

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def dependencies(self) -> Sequence[str]:
        return ("audio",)

    def __init__(self, context):
        super().__init__(context)
        self._engine = TTSFactory.create()

    async def initialize(self) -> None:
        pass

    async def start(self) -> None:
        self.context.logger.info("tts_started")

    async def stop(self) -> None:
        pass

    async def shutdown(self) -> None:
        pass

    async def speak(self, text: str) -> None:
        self._engine.speak(text)

    async def health(self) -> dict:
        return {
            "service": self.name,
            "status": HealthStatus.HEALTHY.value,
        }

    async def status(self) -> dict:
        return {
            "service": self.name,
            "ready": True,
        }
