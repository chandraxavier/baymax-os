"""
Baymax OS Configuration Loader
"""

from __future__ import annotations

from pathlib import Path

import yaml

from baymax.core.configuration.models import Configuration
from baymax.core.configuration.validator import ConfigurationValidator


class ConfigurationLoader:
    """Loads Baymax configuration from YAML files."""

    def __init__(self, config_root: Path) -> None:
        self._config_root = config_root

    def load(self) -> Configuration:
        """
        Load configuration from the default system.yaml file.
        """
        config_file = self._config_root / "defaults" / "system.yaml"

        if not config_file.exists():
            return Configuration()

        with config_file.open("r", encoding="utf-8") as stream:
            data = yaml.safe_load(stream) or {}

        configuration = Configuration.model_validate(data)
        return ConfigurationValidator.validate(configuration)
