# Baymax OS Architecture

Baymax OS is an automotive operating system for a 2013 Suzuki Ritz VDi ABS.
It is not a Raspberry Pi dashboard. The Raspberry Pi 4 is the first compute
target, but the platform architecture is designed around runtime ownership,
service isolation, hardware abstraction, and event-driven communication.

## Core Layers

Baymax is organized into long-lived architectural layers:

- Runtime: owns boot, shutdown, runtime state, and core manager wiring.
- Configuration: loads and validates typed system configuration.
- Logging: provides the shared service-aware logging foundation.
- Event Bus: will route communication between services.
- Service Manager: will register services, resolve dependencies, and enforce
  lifecycle ordering.
- HAL: isolates vehicle and device hardware from service logic.
- Services: implement vehicle, UI, connectivity, automation, and diagnostics
  behavior through the Baymax service contract.

## Runtime Ownership

The Runtime Engine owns the platform lifecycle. It creates the immutable
`RuntimeContext` and injects core dependencies into services. Services do not
instantiate core managers, read YAML files, or control other services directly.

Current Sprint 1 runtime boot initializes:

1. Runtime state lifecycle.
2. Configuration manager.
3. Logging foundation.
4. Runtime context.

Service registration and dependency-ordered startup will be added through the
Service Manager without changing the service contract.

## Service Communication

Services communicate through events. Direct service-to-service business calls
are not part of the architecture because they create hidden lifecycle and
availability coupling.

## Hardware Access

Vehicle hardware, sensors, cameras, lighting, Bluetooth, OBD-II, and future CAN
support belong behind the Hardware Abstraction Layer. Services consume HAL
capabilities through injected platform dependencies and events.

## Production Rules

- Python code targets Python 3.13.
- Public interfaces use type hints and docstrings.
- Runtime code uses logging after the boot banner.
- Configuration is typed and validated.
- Documentation changes accompany implementation changes.
