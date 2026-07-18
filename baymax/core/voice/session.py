from baymax.core.personality.loader import PersonalityLoader
from baymax.services.tts.engine import TTSFactory


class VoiceSession:
    def __init__(self, provider="console"):
        self.personality = PersonalityLoader().load()
        self.tts = TTSFactory.create(provider)

    def startup(self):
        self.tts.speak(self.personality["greetings"]["startup"][0])

    def say(self, text):
        self.tts.speak(text)


if __name__ == "__main__":
    session = VoiceSession()
    session.startup()
    session.say("Systems online.")
