"""
Baymax Runtime Context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class RuntimeContext:
    """
    Immutable runtime context shared by all Baymax services.
    """

    platform_version: str
    development_mode: bool
    configuration: Any
    logger: Any
    events: Any
    registry: Any
    health: Any
    service_manager: Any = field(default=None)
