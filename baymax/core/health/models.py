"""
Core health models for Baymax OS.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class HealthStatus(str, Enum):
    """Standard health states for runtime and services."""

    UNKNOWN = "unknown"
    HEALTHY = "healthy"
    WARNING = "warning"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


@dataclass(frozen=True, slots=True)
class HealthReport:
    """Health information returned by a Baymax component."""

    service: str
    status: HealthStatus
    message: str = ""
    version: str = ""
    uptime_seconds: int = 0
    details: dict[str, Any] = field(default_factory=dict)
    last_updated: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def as_dict(self) -> dict[str, Any]:
        """Return a JSON-compatible health payload."""

        return {
            "service": self.service,
            "status": self.status.value,
            "message": self.message,
            "version": self.version,
            "uptime_seconds": self.uptime_seconds,
            "details": self.details,
            "last_updated": self.last_updated.isoformat(),
        }
