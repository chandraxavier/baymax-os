from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[3]
CONFIG_DIR = ROOT / "shared" / "config"


class ConfigLoader:

    @staticmethod
    def load(filename: str):
        path = CONFIG_DIR / filename

        if not path.exists():
            raise FileNotFoundError(path)

        with open(path, "r") as f:
            return yaml.safe_load(f)