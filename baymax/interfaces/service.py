"""
Baymax OS Service Contract

Defines the abstract base class implemented by every Baymax OS service.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence

from baymax.core.runtime.context import RuntimeContext


class BaymaxService(ABC):
    """
    Abstract base class for every Baymax OS service.

    All services managed by the Runtime Engine must inherit from this class.
    """

    def __init__(self, context: RuntimeContext) -> None:
        self._context = context

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique service name."""
        ...

    @property
    @abstractmethod
    def version(self) -> str:
        """Semantic version of the service."""
        ...

    @property
    @abstractmethod
    def dependencies(self) -> Sequence[str]:
        """Services that must start before this service."""
        ...

    @property
    def context(self) -> RuntimeContext:
        """Shared runtime context."""
        return self._context

    @abstractmethod
    async def initialize(self) -> None:
        """Initialize resources."""
        ...

    @abstractmethod
    async def start(self) -> None:
        """Start the service."""
        ...

    @abstractmethod
    async def stop(self) -> None:
        """Stop the service."""
        ...

    async def restart(self) -> None:
        """Restart the service."""

        await self.stop()
        await self.start()

    @abstractmethod
    async def shutdown(self) -> None:
        """Release resources and perform cleanup."""
        ...

    @abstractmethod
    async def health(self) -> dict:
        """Return current service health information."""
        ...

    @abstractmethod
    async def status(self) -> dict:
        """Return current service lifecycle status."""
        ...
