"""
Boot entry points for Baymax OS.
"""

from __future__ import annotations

from pathlib import Path

from baymax.core.runtime.context import RuntimeContext
from baymax.core.runtime.engine import RuntimeEngine


BOOT_BANNER = """
============================================================
Baymax OS
Automotive Runtime Engine
============================================================
""".strip()


def boot_runtime(config_root: Path) -> RuntimeContext:
    """
    Boot the Baymax Runtime Engine and return its context.

    This is the only core runtime function allowed to print because the boot
    banner must be visible before logging has been initialized.
    """

    print(BOOT_BANNER)
    engine = RuntimeEngine(config_root=config_root)
    return engine.boot()
