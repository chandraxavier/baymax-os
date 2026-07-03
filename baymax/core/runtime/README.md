# Baymax Runtime

The runtime package owns Baymax OS boot, shutdown, and runtime state.

## Modules

- `state.py`: runtime lifecycle state definitions and allowed transitions.
- `lifecycle.py`: transition validation and transition history.
- `engine.py`: boot and shutdown coordinator for core infrastructure.
- `context.py`: immutable dependency-injection context shared with services.
- `boot.py`: boot banner and process entry helper.

## Current Behavior

`RuntimeEngine.boot()` loads configuration, configures logging, creates
`RuntimeContext`, and moves the runtime to `running`.

`RuntimeEngine.shutdown()` moves a running or degraded runtime through
`stopping` to `stopped`.

## Design Rules

- Runtime owns managers.
- Services receive dependencies through `RuntimeContext`.
- Services do not read configuration files directly.
- Runtime uses logging after the boot banner.
- Service startup order belongs to the Service Manager.
