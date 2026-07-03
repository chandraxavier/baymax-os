"""
Baymax OS Configuration Validator
"""

from __future__ import annotations

from baymax.core.configuration.models import Configuration


class ConfigurationValidator:
    """
    Validates Baymax configuration.
    """

    @staticmethod
    def validate(configuration: Configuration) -> Configuration:
        """
        Validate the configuration.

        Currently, Pydantic performs structural validation.
        This class is reserved for additional business rules.
        """
        if configuration.network.mqtt_port <= 0:
            raise ValueError("MQTT port must be greater than zero.")

        if not configuration.system.name:
            raise ValueError("System name cannot be empty.")

        return configuration
