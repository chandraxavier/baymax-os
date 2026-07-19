"""
Baymax Audio models.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class AudioDeviceType(str, Enum):
    SINK = "sink"
    SOURCE = "source"


class AudioDeviceState(str, Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


@dataclass(slots=True)
class AudioDeviceInfo:
    id: int
    name: str
    description: str
    device_type: AudioDeviceType
    state: AudioDeviceState
    default: bool = False
