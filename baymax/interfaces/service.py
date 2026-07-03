"""
Baymax OS Service Interface

Defines the contract implemented by every Baymax service.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence


class ServiceInterface(ABC):
    """
    Base interface for all Baymax services.

    Every service managed by the Runtime Engine must implement
    this interface.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique service name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def version(self) -> str:
        """Service version."""
        raise NotImplementedError

    @property
    @abstractmethod
    def dependencies(self) -> Sequence[str]:
        """Names of services required before this service starts."""
        raise NotImplementedError

    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the service."""
        raise NotImplementedError

    @abstractmethod
    async def start(self) -> None:
        """Start the service."""
        raise NotImplementedError

    @abstractmethod
    async def stop(self) -> None:
        """Stop the service."""
        raise NotImplementedError

    @abstractmethod
    async def shutdown(self) -> None:
        """Shutdown and release resources."""
        raise NotImplementedError

    @abstractmethod
    async def health(self) -> dict:
        """Return the service health."""
        raise NotImplementedError
