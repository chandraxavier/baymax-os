"""
Audio hardware discovery probe.
"""

from __future__ import annotations

from baymax.services.audio.manager import AudioManager
from baymax.services.device.models import Device, DeviceState, DeviceType
from baymax.services.device.probes.base import DeviceProbe


class AudioProbe(DeviceProbe):
    """Discovers PipeWire audio devices."""

    @property
    def name(self) -> str:
        return "audio"

    def discover(self) -> list[Device]:
        manager = AudioManager()
        devices: list[Device] = []

        for output in manager.list_outputs():
            devices.append(
                Device(
                    id=f"audio-output-{output.id}",
                    name=output.description,
                    device_type=DeviceType.AUDIO,
                    state=DeviceState.AVAILABLE,
                    metadata={
                        "kind": "output",
                        "default": str(output.default),
                    },
                )
            )

        for source in manager.list_inputs():
            devices.append(
                Device(
                    id=f"audio-input-{source.id}",
                    name=source.description,
                    device_type=DeviceType.AUDIO,
                    state=DeviceState.AVAILABLE,
                    metadata={
                        "kind": "input",
                        "default": str(source.default),
                    },
                )
            )

        return devices
