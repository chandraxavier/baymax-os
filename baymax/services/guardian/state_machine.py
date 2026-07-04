"""
Baymax Guardian State Machine

This module defines the operating states of Baymax OS.

Guardian transitions between these states based on runtime events, health
checks, and shutdown requests.
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
