from baymax.services.audio.manager import AudioManager

audio = AudioManager()

print("=" * 50)
print("Baymax Audio Test")
print("=" * 50)

outputs = audio.list_outputs()
inputs = audio.list_inputs()

print(f"Outputs : {len(outputs)}")
for device in outputs:
    print(f"  [{device.id}] {device.description} (default={device.default})")

print()

print(f"Inputs  : {len(inputs)}")
for device in inputs:
    print(f"  [{device.id}] {device.description} (default={device.default})")

print()

print(f"Volume  : {audio.get_volume()}%")
print("=" * 50)
