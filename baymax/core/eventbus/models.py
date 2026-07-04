"""
Event models for Baymax OS.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class EventTopic(str, Enum):
    """Core event topics published by the platform."""

    RUNTIME_READY = "runtime.ready"
    RUNTIME_STOPPING = "runtime.stopping"
    SERVICE_INITIALIZED = "service.initialized"
    SERVICE_STARTED = "service.started"
    SERVICE_STOPPED = "service.stopped"
    SERVICE_FAILED = "service.failed"
    HEALTH_UPDATED = "health.updated"
    GUARDIAN_READY = "guardian.ready"


@dataclass(frozen=True, slots=True)
class Event:
    """Immutable event delivered through the Baymax event bus."""

    topic: str
    source: str
    payload: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


EventHandler = Callable[[Event], Awaitable[None] | None]
