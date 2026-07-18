from pathlib import Path
import yaml


class PersonalityLoader:
    """Loads a personality definition from YAML files."""

    def __init__(self, personality: str = "tinker"):
        self.base = (
            Path(__file__).resolve().parents[2]
            / "personalities"
            / personality
        )

    def _load(self, filename: str) -> dict:
        file = self.base / filename
        with open(file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def load(self) -> dict:
        return {
            "personality": self._load("personality.yaml"),
            "speech": self._load("speech.yaml"),
            "emotions": self._load("emotions.yaml"),
            "greetings": self._load("greetings.yaml"),
            "callbacks": self._load("callbacks.yaml"),
            "rules": self._load("rules.yaml"),
        }


if __name__ == "__main__":
    from pprint import pprint

    pprint(PersonalityLoader().load())
