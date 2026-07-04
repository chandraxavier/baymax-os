"""
Baymax OS Runtime Context

Provides read-only access to shared runtime infrastructure for all
Baymax services.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import uuid4


@dataclass(frozen=True, slots=True)
class RuntimeContext:
    """
    Immutable runtime context shared across all Baymax services.

    This object is created once during boot by the Runtime Engine and
    passed to every service managed by the platform.
    """

    platform_version: str
    development_mode: bool = False

    configuration: Any | None = None
    logger: Any | None = None
    events: Any | None = None
    registry: Any | None = None
    service_manager: Any | None = None
    health: Any | None = None

    runtime_id: str = field(default_factory=lambda: str(uuid4()))
    boot_time: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    @property
    def uptime(self) -> timedelta:
        """
        Return the current runtime uptime.
        """
        return datetime.now(timezone.utc) - self.boot_time
