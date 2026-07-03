# Boot Sequence

Baymax OS boots as an automotive operating system. Linux and systemd are process
hosts; they are not the Baymax architecture.

## Sprint 1 Boot Path

```
Power On
  -> Linux
  -> systemd
  -> baymaxd
  -> Runtime Engine
  -> Configuration Manager
  -> Logging Foundation
  -> Runtime Context
  -> Service Manager
  -> Guardian Service
  -> Guardian Console
  -> Dashboard
```

The implemented Sprint 1 runtime reaches `Runtime Context`. Service Manager,
Guardian Service startup, Guardian Console, and Dashboard launch remain the next
runtime layers.

## Runtime Transitions

During a successful boot the Runtime Engine transitions:

```
created -> booting -> configuring -> initializing -> running
```

If configuration, logging, or context creation fails, the Runtime Engine moves
to `failed` and logs the exception.

## Boot Banner

The boot banner is emitted before logging is configured. After that point,
runtime and service code must use the Baymax logging foundation.
