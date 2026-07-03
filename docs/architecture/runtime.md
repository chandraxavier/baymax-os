# Runtime Architecture

The Baymax Runtime Engine is the owner of operating system lifecycle. It is
responsible for moving Baymax from process start to a usable runtime context and
eventually through graceful shutdown.

## Responsibilities

- Maintain runtime state using `RuntimeLifecycle`.
- Load platform configuration through `ConfigurationManager`.
- Configure the core logging foundation.
- Create the immutable `RuntimeContext`.
- Provide a stable boot surface through `boot_runtime`.
- Prepare the execution boundary for the future Service Manager.

## Runtime States

Runtime state is defined in `baymax.core.runtime.state.RuntimeState`.

```
CREATED
  -> BOOTING
  -> CONFIGURING
  -> INITIALIZING
  -> RUNNING
  -> STOPPING
  -> STOPPED
```

Failure paths move the runtime to `FAILED`. A degraded runtime can recover to
`RUNNING` or stop cleanly.

## Runtime Context

`RuntimeContext` is immutable and created once during boot. It carries shared
platform infrastructure to services:

- platform version
- development mode
- configuration manager
- logger
- event bus, when implemented
- service registry, when implemented

Services receive the context through dependency injection. They must not create
their own core managers.

## Current Sprint 1 Boundary

The Runtime Engine currently boots core infrastructure only. Service
registration, dependency resolution, service health aggregation, and event bus
wiring are intentionally reserved for the Service Manager and later runtime
increments.
