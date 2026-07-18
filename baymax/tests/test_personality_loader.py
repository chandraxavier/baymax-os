from baymax.core.personality.loader import PersonalityLoader

loader = PersonalityLoader()
personality = loader.load()

assert personality["personality"]["name"] == "Tinker"
assert personality["speech"]["voice"]["name"] == "Tinker"
assert personality["emotions"]["default"] == "calm"

print("✅ Tinker personality loaded successfully.")
