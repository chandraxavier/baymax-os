# Baymax OS Service Contract

**Version:** 1.0
**Status:** Approved
**Owner:** Baymax Core Architecture

---

# Purpose

This document defines the contract that every Baymax OS service must implement.

The objective is to ensure every service behaves consistently, regardless of implementation language or hardware platform.

Services are managed exclusively by the Runtime Engine.

---

# Design Principles

Every service shall be:

- Modular
- Loosely coupled
- Highly cohesive
- Event-driven
- Hardware independent
- Offline first
- Privacy first
- Production ready
- Observable
- Testable

No service shall directly manage another service.

No service shall directly access another service's internal state.

---

# Service Lifecycle

Every service follows the same lifecycle.

```
CREATED
    │
    ▼
INITIALIZED
    │
    ▼
STARTING
    │
    ▼
RUNNING
    │
 ┌──┴─────────────┐
 ▼                ▼
DEGRADED       STOPPING
 │                │
 ▼                ▼
FAILED        STOPPED
```

Only the Runtime Engine may transition services between states.

---

# Service Interface

Every service shall implement:

- initialize()
- start()
- stop()
- shutdown()
- health()

Every service must expose:

- name
- version
- dependencies

---

# Dependency Management

Dependencies are declared only.

Example:

Vehicle Service

depends on

- Configuration
- Logging
- Event Bus

The Runtime Engine resolves startup order.

Services shall never start dependencies directly.

---

# Runtime Context

Every service receives a RuntimeContext.

Services shall never instantiate core services.

Example:

```
RuntimeContext

Configuration

Logger

Event Bus

Service Registry
```

Dependencies are provided by the Runtime Engine.

---

# Communication

Services communicate only through events.

Incorrect

```
Vehicle -> Guardian
```

Correct

```
Vehicle

↓

Event Bus

↓

Guardian
```

No service shall directly invoke another service for business logic.

---

# Configuration

Services never read configuration files.

Services request configuration from the Configuration Service.

Example

```
configuration.vehicle

configuration.network

configuration.logging
```

---

# Logging

Services never print to stdout.

Services use the Logging Service.

All logs shall include:

- timestamp
- service
- level
- message

Structured logging is mandatory.

---

# Health Reporting

Every service exposes health.

Health states:

- Healthy
- Warning
- Degraded
- Unhealthy

Health reports include:

- service
- status
- uptime
- version
- details

---

# Error Handling

Services shall fail gracefully.

Unexpected failures transition the service to:

FAILED

The Runtime Engine determines recovery strategy.

---

# Startup Order

The official Baymax startup sequence:

Linux

↓

systemd

↓

baymaxd

↓

Runtime Engine

↓

Configuration Service

↓

Logging Service

↓

Event Bus

↓

Service Registry

↓

Guardian Service

↓

Guardian Console

↓

Dashboard

---

# Shutdown

Shutdown occurs in reverse dependency order.

Applications

↓

Guardian

↓

Vehicle

↓

Event Bus

↓

Logging

↓

Configuration

↓

Runtime Engine

---

# Hardware Access

Services shall never access hardware directly.

Hardware access occurs only through the Hardware Abstraction Layer (HAL).

---

# Testing Requirements

Every service must include:

- Unit Tests
- Integration Tests
- Health Tests

Hardware-dependent services additionally require:

- Hardware-in-the-Loop testing

---

# Documentation Requirements

Every service must contain:

README.md

Unit Tests

Public Interfaces

Health Definition

Configuration Schema

---

# Versioning

Every service follows Semantic Versioning.

Example:

1.0.0# Non-Goals

A service shall not:

- Read YAML directly
- Spawn unmanaged threads
- Access hardware directly
- Store global state
- Start or stop other services
- Depend on implementation details of another service

1.1.0

2.0.0

---

# Future Compatibility

The service contract is designed to support:

- Multiple vehicles
- Multiple compute platforms
- Python
- Rust
- C++
- AI accelerators
- Distributed services

without changing the Runtime Engine.

# Non-Goals

A service shall not:

- Read YAML directly
- Spawn unmanaged threads
- Access hardware directly
- Store global state
- Start or stop other services
- Depend on implementation details of another service
