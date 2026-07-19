"""
Baymax Audio Manager.
"""

from __future__ import annotations

import re
import subprocess

from baymax.services.audio.models import AudioDeviceInfo, AudioDeviceState, AudioDeviceType


class AudioManager:
    """Manages PipeWire audio devices."""

    def list_outputs(self) -> list[AudioDeviceInfo]:
        devices: list[AudioDeviceInfo] = []

        try:
            output = subprocess.check_output(["wpctl", "status"], text=True)

            in_sinks = False

            for line in output.splitlines():
                if "Sinks:" in line:
                    in_sinks = True
                    continue

                if in_sinks and not line.strip():
                    break

                if not in_sinks:
                    continue

                match = re.search(r"(\*)?\s*([0-9]+)\.\s+(.*?)\s+\[", line)
                if not match:
                    continue

                default = bool(match.group(1))
                device_id = int(match.group(2))
                description = match.group(3).strip()

                devices.append(
                    AudioDeviceInfo(
                        id=device_id,
                        name=description,
                        description=description,
                        device_type=AudioDeviceType.SINK,
                        state=AudioDeviceState.AVAILABLE,
                        default=default,
                    )
                )

        except Exception:
            pass

        return devices

    def list_inputs(self) -> list[AudioDeviceInfo]:
        """Return available microphone devices."""

        devices: list[AudioDeviceInfo] = []

        try:
            import re
            output = subprocess.check_output(["wpctl", "status"], text=True)

            in_sources = False

            for line in output.splitlines():
                if "Sources:" in line:
                    in_sources = True
                    continue

                if in_sources and not line.strip():
                    break

                if not in_sources:
                    continue

                match = re.search(r"(\*)?\s*([0-9]+)\.\s+(.*?)\s+\[", line)
                if not match:
                    continue

                devices.append(
                    AudioDeviceInfo(
                        id=int(match.group(2)),
                        name=match.group(3).strip(),
                        description=match.group(3).strip(),
                        device_type=AudioDeviceType.SOURCE,
                        state=AudioDeviceState.AVAILABLE,
                        default=bool(match.group(1)),
                    )
                )

        except Exception:
            pass

        return devices

    def get_volume(self) -> int:
        """Return current default output volume percentage."""

        try:
            output = subprocess.check_output(
                ["wpctl", "get-volume", "@DEFAULT_AUDIO_SINK@"],
                text=True,
            ).strip()

            parts = output.split()
            if len(parts) >= 2:
                return round(float(parts[1]) * 100)

        except Exception:
            pass

        return 0

    def set_volume(self, percent: int) -> bool:
        """Set default output volume."""

        percent = max(0, min(100, percent))

        try:
            subprocess.run(
                [
                    "wpctl",
                    "set-volume",
                    "@DEFAULT_AUDIO_SINK@",
                    f"{percent}%",
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False

    def mute(self) -> bool:
        """Mute the default output."""

        try:
            subprocess.run(
                [
                    "wpctl",
                    "set-mute",
                    "@DEFAULT_AUDIO_SINK@",
                    "1",
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False

    def unmute(self) -> bool:
        """Unmute the default output."""

        try:
            subprocess.run(
                [
                    "wpctl",
                    "set-mute",
                    "@DEFAULT_AUDIO_SINK@",
                    "0",
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False
