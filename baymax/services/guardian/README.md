# Baymax Guardian

## Purpose

Baymax Guardian is the runtime supervisor of Baymax OS.

Guardian is the first Baymax component started after Linux boots and is responsible for orchestrating the operating system lifecycle.

## Responsibilities

- Boot orchestration
- System initialization
- Configuration loading
- Service lifecycle management
- Health monitoring
- Boot diagnostics
- Recovery mode
- Safe mode
- Developer mode
- Connectivity initialization
- Guardian Console

## Guardian DOES NOT own

- Vehicle logic
- OBD communication
- Dashboard rendering
- Pulse
- Vision
- Navigation
- AI
- Home Assistant
- Media playback

## Boot Sequence

Power On
↓
Linux
↓
Baymax Guardian
↓
Load Configuration
↓
Initialize Logging
↓
Initialize Event Bus
↓
Start Service Manager
↓
Initialize Connectivity
↓
Launch Guardian Console
↓
Launch Dashboard

## Design Principles

- Linux is an implementation detail.
- Guardian is the operating system runtime.
- Dashboard is an application.
- Every service has an independent lifecycle.
- Hardware access is performed only through HAL.
- Services communicate using events rather than direct dependencies.
- Safety before convenience.
- Offline first.
- Privacy first.

