from baymax.services.device.manager import DeviceManager
from baymax.services.device.probes.audio import AudioProbe

manager = DeviceManager()
manager.register_probe(AudioProbe())

devices = manager.discover()

print("=" * 60)
print("Baymax Device Manager")
print("=" * 60)

print(f"Devices Found : {len(devices)}")
print()

for device in devices:
    print(
        f"{device.device_type.value:10} "
        f"{device.name:35} "
        f"{device.state.value}"
    )

print("=" * 60)
