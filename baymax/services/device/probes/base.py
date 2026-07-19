"""
Base interface for hardware discovery probes.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from baymax.services.device.models import Device


class DeviceProbe(ABC):
    """Base class for all hardware discovery plugins."""

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def discover(self) -> list[Device]:
        """Return all devices discovered by this probe."""
        ...
