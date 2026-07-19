"""
Baymax Vehicle Manager.
"""

from __future__ import annotations

from baymax.services.vehicle.models import VehicleState, VehicleTelemetry


class VehicleManager:
    """Coordinates vehicle telemetry."""

    def __init__(self) -> None:
        self._state = VehicleState.OFFLINE
        self._telemetry = VehicleTelemetry()

    @property
    def state(self) -> VehicleState:
        return self._state

    @property
    def telemetry(self) -> VehicleTelemetry:
        return self._telemetry

    def set_state(self, state: VehicleState) -> None:
        self._state = state

    def update(self, telemetry: VehicleTelemetry) -> None:
        self._telemetry = telemetry
