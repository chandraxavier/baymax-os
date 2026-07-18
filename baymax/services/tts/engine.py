import yaml
from pathlib import Path
from baymax.services.tts.providers.console import ConsoleTTSEngine
from baymax.services.tts.providers.piper import PiperTTSEngine

class TTSFactory:
    @staticmethod
    def create():
        config = yaml.safe_load((Path(__file__).resolve().parents[2] / "config" / "tts.yaml").read_text())
        provider = config.get("provider", "console")
        if provider == "console":
            return ConsoleTTSEngine()
        if provider == "piper":
            return PiperTTSEngine(
                model_path=config["piper"]["model"],
                executable=config["piper"]["executable"],
            )
        raise ValueError(f"Unknown provider: {provider}")

if __name__ == "__main__":
    TTSFactory.create().speak("Hello, Chandra. I'm Tinker.")
