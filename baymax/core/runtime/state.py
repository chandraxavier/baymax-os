"""
Runtime state model for Baymax OS.
"""

from __future__ import annotations

from enum import Enum


class RuntimeState(str, Enum):
    """Lifecycle states owned by the Baymax Runtime Engine."""

    CREATED = "created"
    BOOTING = "booting"
    CONFIGURING = "configuring"
    INITIALIZING = "initializing"
    RUNNING = "running"
    DEGRADED = "degraded"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


RUNTIME_STATE_TRANSITIONS: dict[RuntimeState, set[RuntimeState]] = {
    RuntimeState.CREATED: {RuntimeState.BOOTING},
    RuntimeState.BOOTING: {
        RuntimeState.CONFIGURING,
        RuntimeState.FAILED,
    },
    RuntimeState.CONFIGURING: {
        RuntimeState.INITIALIZING,
        RuntimeState.FAILED,
    },
    RuntimeState.INITIALIZING: {
        RuntimeState.RUNNING,
        RuntimeState.DEGRADED,
        RuntimeState.FAILED,
    },
    RuntimeState.RUNNING: {
        RuntimeState.DEGRADED,
        RuntimeState.STOPPING,
        RuntimeState.FAILED,
    },
    RuntimeState.DEGRADED: {
        RuntimeState.RUNNING,
        RuntimeState.STOPPING,
        RuntimeState.FAILED,
    },
    RuntimeState.STOPPING: {
        RuntimeState.STOPPED,
        RuntimeState.FAILED,
    },
    RuntimeState.STOPPED: {
        RuntimeState.BOOTING,
    },
    RuntimeState.FAILED: {
        RuntimeState.STOPPING,
        RuntimeState.STOPPED,
    },
}
