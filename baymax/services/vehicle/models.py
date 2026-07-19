"""
Baymax Vehicle Models.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class VehicleState(str, Enum):
    OFFLINE = "offline"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RUNNING = "running"
    ERROR = "error"


@dataclass(slots=True)
class VehicleTelemetry:
    rpm: float | None = None
    speed: float | None = None
    coolant_temperature: float | None = None
    fuel_level: float | None = None
    battery_voltage: float | None = None
    engine_load: float | None = None
    intake_air_temperature: float | None = None
    diagnostic_trouble_codes: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
