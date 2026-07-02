"""
Baymax Guardian State Machine

This module defines the operating states of Baymax OS.

The state machine is the single source of truth for the lifecycle of the
Baymax operating system. Guardian transitions between these states based on
system events, health checks, and user actions.

Implementation will be added in a later sprint.
"""

from enum import Enum


class GuardianState(str, Enum):
    """Operating states for Baymax Guardian."""

    POWER_OFF = "power_off"

    BOOTING = "booting"

    INITIALIZING = "initializing"

    CHECKING_STORAGE = "checking_storage"

    CHECKING_CONFIGURATION = "checking_configuration"

    CHECKING_NETWORK = "checking_network"

    STARTING_SERVICES = "starting_services"

    STARTING_DASHBOARD = "starting_dashboard"

    RUNNING = "running"

    DEGRADED = "degraded"

    RECOVERY = "recovery"

    SAFE_MODE = "safe_mode"

    SHUTTING_DOWN = "shutting_down"

    REBOOTING = "rebooting"
    
    POWERING_OFF = "powering_off"
