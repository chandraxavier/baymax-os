"""
Unit tests for the Baymax Runtime Engine.
"""

from __future__ import annotations

import logging
import shutil
import unittest
from pathlib import Path

from baymax.core.runtime.engine import RuntimeEngine
from baymax.core.runtime.state import RuntimeState


class RuntimeEngineTests(unittest.TestCase):
    """Validate runtime boot and shutdown behavior."""

    def setUp(self) -> None:
        self.fixture_root = Path(".test-runtime-engine")
        defaults = self.fixture_root / "defaults"
        defaults.mkdir(parents=True, exist_ok=True)
        (defaults / "system.yaml").write_text(
            "\n".join(
                [
                    "logging:",
                    "  level: INFO",
                    "  directory: .test-runtime-engine/logs",
                    "  json_logging: true",
                ]
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        logging.shutdown()
        shutil.rmtree(self.fixture_root, ignore_errors=True)

    def test_boot_creates_runtime_context_and_starts_guardian(self) -> None:
        engine = RuntimeEngine(config_root=self.fixture_root)

        context = engine.boot()

        self.assertIs(context.service_manager, engine.service_manager)
        self.assertIsNotNone(context.events)
        self.assertIsNotNone(context.health)
        self.assertEqual(engine.state, RuntimeState.RUNNING)
        self.assertEqual(
            engine.service_manager.status("guardian").state.value,
            "running",
        )

        engine.shutdown()
        self.assertEqual(engine.state, RuntimeState.STOPPED)


if __name__ == "__main__":
    unittest.main()
