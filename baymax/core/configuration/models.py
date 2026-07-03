"""
Baymax OS Configuration Models

Defines the strongly typed configuration models used throughout
the Baymax platform.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class SystemConfig(BaseModel):
    """System configuration."""

    name: str = "Baymax OS"
    version: str = "0.1.0"
    development_mode: bool = False


class VehicleConfig(BaseModel):
    """Vehicle configuration."""

    manufacturer: str = "Maruti Suzuki"
    model: str = "Ritz"
    variant: str = "VDi ABS"
    year: int = 2013


class NetworkConfig(BaseModel):
    """Network configuration."""

    hostname: str = "baymax"
    mqtt_host: str = "localhost"
    mqtt_port: int = 1883
    wifi_enabled: bool = True


class LoggingConfig(BaseModel):
    """Logging configuration."""

    level: str = "INFO"
    directory: str = "logs"
    json_logging: bool = True


class GuardianConfig(BaseModel):
    """Guardian configuration."""

    kiosk_mode: bool = True
    auto_launch_dashboard: bool = True


class Configuration(BaseModel):
    """
    Root configuration model.
    """

    system: SystemConfig = Field(default_factory=SystemConfig)
    vehicle: VehicleConfig = Field(default_factory=VehicleConfig)
    network: NetworkConfig = Field(default_factory=NetworkConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    guardian: GuardianConfig = Field(default_factory=GuardianConfig)
