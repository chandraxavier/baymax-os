from pathlib import Path
import socket
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.append(str(ROOT))

from software.plugins.system.plugin import SystemPlugin


class SystemService:
    @staticmethod
    def status():
        return SystemPlugin.get_status()

    @staticmethod
    def info():
        return {
            "hostname": socket.gethostname(),
            "version": "0.1.0",
            "vehicle": {
                "name": "Ritz",
                "model": "VDi ABS",
                "year": 2013
            },
            "platform": "Raspberry Pi 4",
            "status": "online"
        }
