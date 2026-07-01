from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.append(str(ROOT))

from software.plugins.system.plugin import SystemPlugin


class SystemService:

    @staticmethod
    def status():
        return SystemPlugin.get_status()
