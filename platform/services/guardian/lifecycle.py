"""
Baymax Guardian Service Lifecycle

Every Baymax service must implement this lifecycle.

Guardian uses these states to supervise, monitor and recover services.
"""

from enum import Enum


class ServiceState(str, Enum):
    """Standard lifecycle states for all Baymax services."""

    CREATED = "created"

    INITIALIZED = "initialized"

    STARTING = "starting"

    RUNNING = "running"

    DEGRADED = "degraded"

    FAILED = "failed"

    STOPPING = "stopping"

    STOPPED = "stopped"


SERVICE_STATE_TRANSITIONS = {
    ServiceState.CREATED: [
        ServiceState.INITIALIZED,
    ],

    ServiceState.INITIALIZED: [
        ServiceState.STARTING,
        ServiceState.STOPPED,
    ],

    ServiceState.STARTING: [
        ServiceState.RUNNING,
        ServiceState.FAILED,
    ],

    ServiceState.RUNNING: [
        ServiceState.DEGRADED,
        ServiceState.FAILED,
        ServiceState.STOPPING,
    ],

    ServiceState.DEGRADED: [
        ServiceState.RUNNING,
        ServiceState.FAILED,
        ServiceState.STOPPING,
    ],

    ServiceState.FAILED: [
        ServiceState.STARTING,
        ServiceState.STOPPED,
    ],

    ServiceState.STOPPING: [
        ServiceState.STOPPED,
    ],

    ServiceState.STOPPED: [
        ServiceState.STARTING,
    ],
}
