"""
Service manager models for Baymax OS.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class ServiceState(str, Enum):
    """Standard lifecycle states for managed services."""

    CREATED = "created"
    INITIALIZED = "initialized"
    STARTING = "starting"
    RUNNING = "running"
    DEGRADED = "degraded"
    FAILED = "failed"
    STOPPING = "stopping"
    STOPPED = "stopped"


SERVICE_STATE_TRANSITIONS: dict[ServiceState, set[ServiceState]] = {
    ServiceState.CREATED: {ServiceState.INITIALIZED, ServiceState.FAILED},
    ServiceState.INITIALIZED: {
        ServiceState.STARTING,
        ServiceState.STOPPED,
        ServiceState.FAILED,
    },
    ServiceState.STARTING: {ServiceState.RUNNING, ServiceState.FAILED},
    ServiceState.RUNNING: {
        ServiceState.DEGRADED,
        ServiceState.FAILED,
        ServiceState.STOPPING,
    },
    ServiceState.DEGRADED: {
        ServiceState.RUNNING,
        ServiceState.FAILED,
        ServiceState.STOPPING,
    },
    ServiceState.FAILED: {ServiceState.STARTING, ServiceState.STOPPED},
    ServiceState.STOPPING: {ServiceState.STOPPED, ServiceState.FAILED},
    ServiceState.STOPPED: {ServiceState.STARTING},
}


@dataclass(slots=True)
class ServiceStatus:
    """Current service status exposed by the service manager."""

    name: str
    version: str
    state: ServiceState
    dependencies: tuple[str, ...] = ()
    last_changed: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    details: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        """Return a JSON-compatible status payload."""

        return {
            "name": self.name,
            "version": self.version,
            "state": self.state.value,
            "dependencies": list(self.dependencies),
            "last_changed": self.last_changed.isoformat(),
            "details": self.details,
        }
