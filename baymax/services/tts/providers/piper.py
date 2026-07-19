from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from baymax.services.tts.base import BaseTTSEngine
from baymax.services.tts.cleaner import clean_for_speech


class PiperTTSEngine(BaseTTSEngine):

    def __init__(self, model_path: str = "", executable: str = "/usr/local/bin/piper"):
        self.model_path = model_path
        self.executable = executable

    def speak(self, text: str):
        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as f:
            wav_path = Path(f.name)

        subprocess.run(
            [
                self.executable,
                "--model",
                self.model_path,
                "--output_file",
                str(wav_path),
            ],
            input=clean_for_speech(text).encode(),
            check=True,
        )

        subprocess.run(
            ["pw-play", str(wav_path)],
            check=True,
        )

        wav_path.unlink(missing_ok=True)
