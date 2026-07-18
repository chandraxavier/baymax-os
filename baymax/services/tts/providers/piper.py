from baymax.services.tts.base import BaseTTSEngine


class PiperTTSEngine(BaseTTSEngine):
    def __init__(self, model_path: str = "", config_path: str = ""):
        self.model_path = model_path
        self.config_path = config_path

    def speak(self, text: str):
        raise NotImplementedError("Piper TTS provider is not implemented yet.")
