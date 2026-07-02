"""
Baymax Guardian Health Model

Every Baymax service exposes its health using this model.

Guardian uses these health reports for:
- Boot validation
- Service supervision
- Recovery
- Guardian Console
- Diagnostics
"""

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


class HealthStatus(str, Enum):
    """Standard health states."""

    UNKNOWN = "unknown"

    HEALTHY = "healthy"

    WARNING = "warning"

    DEGRADED = "degraded"

    UNHEALTHY = "unhealthy"


@dataclass
class HealthReport:
    """Health information returned by every Baymax service."""

    service: str

    status: HealthStatus

    message: str = ""

    last_updated: Optional[datetime] = None

    uptime_seconds: int = 0

    version: str = ""

    details: dict | None = None
