# Baymax Event Bus

The event bus is the core communication path between Baymax services.

## Responsibilities

- Publish immutable `Event` objects.
- Dispatch events to synchronous or asynchronous handlers.
- Keep services decoupled from each other's implementation details.
- Provide the internal event surface for future MQTT and plugin bridges.

## Core Topics

- `runtime.ready`
- `runtime.stopping`
- `service.initialized`
- `service.started`
- `service.stopped`
- `service.failed`
- `health.updated`
- `guardian.ready`

Services publish events through the `RuntimeContext.events` dependency.
