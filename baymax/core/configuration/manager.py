"""
Baymax OS Configuration Manager
"""

from __future__ import annotations

from pathlib import Path

from baymax.core.configuration.loader import ConfigurationLoader
from baymax.core.configuration.models import (
    Configuration,
    SystemConfig,
)


class ConfigurationManager:
    """
    Central access point for Baymax configuration.
    """

    def __init__(self, config_root: Path) -> None:
        self._loader = ConfigurationLoader(config_root)
        self._configuration: Configuration | None = None

    def load(self) -> None:
        """Load the platform configuration."""
        self._configuration = self._loader.load()

    @property
    def configuration(self) -> Configuration:
        if self._configuration is None:
            raise RuntimeError("Configuration has not been loaded.")
        return self._configuration

    @property
    def system(self) -> SystemConfig:
        return self.configuration.system

    @property
    def vehicle(self):
        return self.configuration.vehicle

    @property
    def network(self):
        return self.configuration.network

    @property
    def logging(self):
        return self.configuration.logging

    @property
    def guardian(self):
        return self.configuration.guardian
