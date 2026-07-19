"""
Baymax Device Manager.
"""

from __future__ import annotations

from baymax.services.device.models import Device
from baymax.services.device.probes.base import DeviceProbe


class DeviceManager:
    """Coordinates hardware discovery through registered probes."""

    def __init__(self) -> None:
        self._probes: list[DeviceProbe] = []

    def register_probe(self, probe: DeviceProbe) -> None:
        """Register a hardware discovery probe."""
        self._probes.append(probe)

    def discover(self) -> list[Device]:
        """Discover all hardware devices."""
        devices: list[Device] = []

        for probe in self._probes:
            try:
                devices.extend(probe.discover())
            except Exception:
                # Ignore individual probe failures so one bad probe
                # does not prevent the rest of the hardware from loading.
                continue

        return devices
