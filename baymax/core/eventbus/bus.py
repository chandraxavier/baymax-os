"""
In-process event bus for Baymax OS.
"""

from __future__ import annotations

import inspect
from collections import defaultdict

from baymax.core.eventbus.models import Event, EventHandler


class EventBus:
    """
    Lightweight asynchronous event dispatcher.

    The bus is intentionally in-process for the core runtime. External bridges
    such as MQTT can subscribe and republish events without changing service
    code.
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(self, topic: str, handler: EventHandler) -> None:
        """Subscribe a handler to an event topic."""

        self._handlers[topic].append(handler)

    def unsubscribe(self, topic: str, handler: EventHandler) -> None:
        """Remove a handler from an event topic."""

        handlers = self._handlers.get(topic, [])
        if handler in handlers:
            handlers.remove(handler)

    async def publish(self, event: Event) -> None:
        """Publish an event to all handlers registered for its topic."""

        handlers = tuple(self._handlers.get(event.topic, ()))

        for handler in handlers:
            result = handler(event)
            if inspect.isawaitable(result):
                await result
