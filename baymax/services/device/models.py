"""
Baymax Device models.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class DeviceType(str, Enum):
    AUDIO = "audio"
    BLUETOOTH = "bluetooth"
    USB = "usb"
    CAMERA = "camera"
    DISPLAY = "display"
    NETWORK = "network"
    OBD = "obd"
    GPS = "gps"
    SENSOR = "sensor"


class DeviceState(str, Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


@dataclass(slots=True)
class Device:
    id: str
    name: str
    device_type: DeviceType
    state: DeviceState
    metadata: dict[str, str]
