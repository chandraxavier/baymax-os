"""
Unit tests for the Baymax event bus.
"""

from __future__ import annotations

import unittest

from baymax.core.eventbus import Event, EventBus


class EventBusTests(unittest.IsolatedAsyncioTestCase):
    """Validate event dispatch behavior."""

    async def test_publish_delivers_event_to_subscriber(self) -> None:
        bus = EventBus()
        received: list[Event] = []

        async def handler(event: Event) -> None:
            received.append(event)

        event = Event(
            topic="runtime.ready",
            source="test",
            payload={"state": "running"},
        )

        bus.subscribe(event.topic, handler)
        await bus.publish(event)

        self.assertEqual(received, [event])


if __name__ == "__main__":
    unittest.main()
