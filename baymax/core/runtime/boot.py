"""
Boot entry points for Baymax OS.
"""

from __future__ import annotations

from pathlib import Path

from baymax.core.runtime.context import RuntimeContext
from baymax.core.runtime.engine import RuntimeEngine


def boot_runtime(config_root: Path) -> RuntimeContext:
    """Boot the Baymax Runtime Engine and return its context."""

    engine = RuntimeEngine(config_root=config_root)
    return engine.boot()
