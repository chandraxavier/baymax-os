"""
Unit tests for Baymax service lifecycle management.
"""

from __future__ import annotations

import unittest
from typing import Sequence

from baymax.core.eventbus import EventBus
from baymax.core.health import HealthManager
from baymax.core.runtime.context import RuntimeContext
from baymax.core.service_manager import (
    ServiceManager,
    ServiceRegistry,
    ServiceState,
)
from baymax.interfaces.service import BaymaxService


class MemoryLogger:
    """Small logger used by service manager unit tests."""

    def info(self, event: str, **kwargs) -> None:
        """Accept structured log events."""


class TestService(BaymaxService):
    """Minimal managed service for lifecycle tests."""

    def __init__(
        self,
        context: RuntimeContext,
        name: str,
        dependencies: Sequence[str] = (),
    ) -> None:
        super().__init__(context)
        self._name = name
        self._dependencies = tuple(dependencies)
        self.calls: list[str] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def dependencies(self) -> Sequence[str]:
        return self._dependencies

    async def initialize(self) -> None:
        self.calls.append("initialize")

    async def start(self) -> None:
        self.calls.append("start")

    async def stop(self) -> None:
        self.calls.append("stop")

    async def shutdown(self) -> None:
        self.calls.append("shutdown")

    async def health(self) -> dict:
        return {
            "status": "healthy",
            "message": "ok",
            "uptime_seconds": 1,
            "details": {},
        }

    async def status(self) -> dict:
        return {"service": self.name}


class ServiceManagerTests(unittest.IsolatedAsyncioTestCase):
    """Validate service manager lifecycle behavior."""

    async def test_start_all_respects_dependencies(self) -> None:
        context = RuntimeContext(platform_version="test")
        manager = ServiceManager(
            registry=ServiceRegistry(),
            events=EventBus(),
            health=HealthManager(),
            logger=MemoryLogger(),
        )
        base = TestService(context, "base")
        dependent = TestService(context, "dependent", dependencies=("base",))

        manager.register(dependent)
        manager.register(base)
        await manager.start_all()

        self.assertEqual(manager.status("base").state, ServiceState.RUNNING)
        self.assertEqual(
            manager.status("dependent").state,
            ServiceState.RUNNING,
        )
        self.assertEqual(base.calls, ["initialize", "start"])
        self.assertEqual(dependent.calls, ["initialize", "start"])


if __name__ == "__main__":
    unittest.main()
