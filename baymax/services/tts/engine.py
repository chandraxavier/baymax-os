from baymax.services.tts.providers.console import ConsoleTTSEngine
from baymax.services.tts.providers.piper import PiperTTSEngine

class TTSFactory:
    _providers = {
        "console": ConsoleTTSEngine,
        "piper": PiperTTSEngine,
    }

    @classmethod
    def create(cls, provider="console"):
        if provider not in cls._providers:
            raise ValueError(f"Unknown TTS provider: {provider}")
        return cls._providers[provider]()

if __name__ == "__main__":
    tts = TTSFactory.create()
    tts.speak("Hello, Chandra. I'm Tinker.")
