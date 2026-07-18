# 🚗 Baymax OS

> **An Open-Source Automotive Cognitive Operating System**

**Documentation Version:** 2.0  
**Last Updated:** 2026-07-18  
**Project Status:** Runtime Foundation Complete

Baymax OS is a production-oriented, open-source automotive operating system designed to transform existing vehicles into intelligent, software-defined platforms.

Inspired by Tesla OS, Android Automotive, Mercedes-Benz MBUX, Rivian, Linux, and modern distributed systems, Baymax OS provides a modular runtime capable of powering diagnostics, vehicle integrations, AI assistants, automation, and intelligent in-car experiences.

> **Baymax OS is NOT a Raspberry Pi dashboard.**

The Raspberry Pi is currently the primary development platform. Baymax OS is designed to be hardware-independent and portable to future automotive-grade hardware.

---

# Vision

Our mission is simple:

> **Build the automotive operating system we wish existed.**

Baymax OS brings modern software engineering principles to both older and newer vehicles while remaining:

- Privacy First
- Offline First
- Modular
- Event Driven
- Hardware Independent
- Open Source
- Production Ready

---

# Baymax Philosophy

Baymax OS is **not** an AI assistant.

Baymax OS is an **Automotive Cognitive Operating System**.

Its purpose is to augment the driver—not replace them.

Every subsystem follows these principles:

- Human in control
- AI assists, never overrides
- Explainable decisions
- Offline by default
- Privacy by design
- Modular architecture
- Safety before convenience

Baymax makes decisions through its **Planner**, executes work through **Skills**, and interacts with the vehicle through **Drivers**.

Large Language Models provide recommendations—not direct control of vehicle hardware.

---

# Current Development Vehicle

## Vehicle

- 2013 Suzuki Ritz VDi ABS

## Development Hardware

- Raspberry Pi 4 (8GB)
- Amazon Fire HD Tablet
- ESP32
- Pioneer SPH-C19BT
- Bluetooth OBD-II Adapter
- Home Assistant Integration

---

# Future Hardware

Baymax OS is designed to scale beyond Raspberry Pi.

Planned hardware includes:

- Automotive-grade SBC
- CAN Bus Interface
- GPS
- Front Dashcam
- Rear Camera
- Driver Monitoring Camera
- AI Accelerator
- LTE / 5G Connectivity
- Ambient Lighting Controllers
- Amplifier
- Environmental Sensors
- Battery Monitoring
- Vehicle Power Controller

---

# Core Principles

## Modular

Every capability is implemented as an independent service.

## Event Driven

Services communicate through the Event Bus.

## Hardware Independent

Vehicle hardware is isolated behind dedicated drivers.

## Offline First

The vehicle remains fully functional without Internet connectivity.

## Privacy First

Vehicle and user data remain local unless explicitly shared.

## Documentation First

Documentation is considered part of the implementation.

A feature is not complete until its documentation has been updated.

---

# Architecture

```
                         Baymax OS

                      Runtime Engine
                            │
                ┌───────────┼────────────┐
                │           │            │
         Configuration   Logging   Runtime Context
                            │
                     Service Manager
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
    Guardian            Planner            Skills
        │                   │                   │
        └─────────────── Event Bus ─────────────┘
                            │
                           Tasks
                            │
         ┌─────────────┬─────────────┬─────────────┐
         │             │             │             │
      Speech         OBD-II     Navigation    Lighting
                            │
                      Hardware Drivers
                            │
              Raspberry Pi / CAN / ESP32
```

---

# Runtime Boot Sequence

```
Power On
   │
Linux
   │
Baymax Runtime
   │
Load Configuration
   │
Initialize Logging
   │
Create Runtime Context
   │
Create Event Bus
   │
Create Health Manager
   │
Create Service Manager
   │
Register Core Services
   │
Start Guardian
   │
Start Planner
   │
Start Skills
   │
Runtime Ready
```

---

# Current Runtime

The Baymax Runtime currently consists of three core services.

## Guardian

Responsible for runtime supervision, lifecycle management and system coordination.

## Planner

Responsible for decision making and task orchestration.

The Planner decides **what** should happen.

## Skills

Responsible for executing capabilities requested by the Planner.

Skills perform the work.

Future skills include:

- Speech
- Navigation
- OBD-II
- Cameras
- Lighting
- Notifications

---

# Repository Structure

```
baymax-os/

├── baymax/
│
├── core/
│   ├── configuration/
│   ├── runtime/
│   ├── logging/
│   ├── eventbus/
│   ├── health/
│   └── service_manager/
│
├── services/
│   ├── guardian/
│   ├── planner/
│   └── skills/
│
├── drivers/
│
├── hal/
│
├── shared/
│
├── docs/
│   ├── architecture/
│   ├── adr/
│   └── development/
│
├── firmware/
├── hardware/
└── scripts/
```

---

# Current Status

## Runtime Foundation

Completed

- Runtime Engine
- Configuration
- Runtime Context
- Structured Logging
- Event Bus
- Health Manager
- Service Manager
- Guardian Runtime
- Planner Runtime
- Skills Runtime
- Event-driven Service Lifecycle
- Graceful Runtime Shutdown

## Current Milestone

Task Execution Pipeline

Planner → Task → Skills

---

# Roadmap

## Phase 1

Runtime Foundation ✅

## Phase 2

Task Pipeline

- Task Model
- Task Dispatcher
- Task Queue

## Phase 3

Core Skills

- Speech
- Notifications
- Diagnostics

## Phase 4

Vehicle Integration

- OBD-II
- CAN
- Sensors

## Phase 5

Companion Experience

- Fire HD Dashboard
- Mobile Companion
- Bluetooth

## Phase 6

AI Platform

- Voice Assistant
- Memory
- Local AI
- Wake Word

## Phase 7

Vision

- Dashcam
- Driver Monitoring
- Object Detection

## Phase 8

Vehicle Intelligence

- Ambient Lighting
- Automation
- Predictive Diagnostics

---

# Development Workflow

```
Documentation
      │
Architecture
      │
Implementation
      │
Testing
      │
Documentation Review
      │
Commit
```

---

# Engineering Rules

Every feature merged into Baymax OS must include:

- Documentation updates
- Architecture review (when required)
- Testing
- Structured logging
- Type hints
- Graceful startup
- Graceful shutdown
- Event-driven communication

Direct hardware access is not permitted outside dedicated drivers.

---

# Technology Stack

- Python 3.13
- Debian Linux
- Docker
- FastAPI
- MQTT
- Home Assistant
- ESP32
- Bluetooth
- GitHub Actions (planned)

---

# Contributing

Please ensure:

- Documentation is updated.
- Architecture remains modular.
- Services remain loosely coupled.
- Pull requests target the correct branch.
- Engineering principles are maintained.

---

# Documentation

```
docs/architecture/
docs/adr/
docs/development/
```

---

# License

This project will be released under the MIT License.

---

# Acknowledgements

Baymax OS is inspired by the engineering excellence of:

- Tesla
- Android Automotive
- Linux
- ROS2
- Mercedes-Benz MBUX
- Rivian
- Open Source Community

---

# The Journey

Baymax OS began as a personal project to modernize a 2013 Suzuki Ritz.

It is evolving into a modular Automotive Cognitive Operating System designed to demonstrate that existing vehicles can benefit from modern software architecture without sacrificing reliability, privacy, safety or openness.

Every commit brings Baymax one step closer to becoming a production-grade automotive operating system.
