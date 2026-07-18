from baymax.services.tts.base import BaseTTSEngine
from baymax.core.personality.loader import PersonalityLoader


class ConsoleTTSEngine(BaseTTSEngine):
    def __init__(self):
        self.personality = PersonalityLoader().load()

    def speak(self, text: str):
        voice = self.personality["speech"]["voice"]["name"]
        print(f"[{voice}] {text}")
