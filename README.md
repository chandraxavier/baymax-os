# Baymax OS

Baymax OS is an open-source automotive operating system for a 2013 Suzuki Ritz
VDi ABS.

## Vision

Baymax OS is not a Raspberry Pi dashboard. It is a modular automotive runtime
for diagnostics, automation, driver assistance, vehicle UI, and future hardware
integrations.

Part of **Thyana Labs**.

## Current Hardware

- Raspberry Pi 4, 8GB
- Amazon Fire HD Tablet
- ESP32
- Pioneer SPH-C19BT
- Bluetooth OBD-II

## Architecture

The platform is built around:

- Runtime Engine
- RuntimeContext
- Configuration Manager
- Logging foundation
- Event Bus
- Service Manager
- Guardian
- Hardware Abstraction Layer

See `ARCHITECTURE.md` and `docs/architecture/` for the current architecture
record.

## Technology Stack

| Layer | Technology |
|--------|------------|
| OS | Raspberry Pi OS Lite |
| Core Runtime | Python 3.13 |
| Backend | FastAPI |
| Frontend | Web UI |
| Messaging | Event Bus, MQTT |
| Database | SQLite |
| Containers | Docker |
| Vision | OpenCV |
| Automation | Home Assistant |

## Repository Structure

```
baymax/
docs/
software/
```

## Roadmap

See `ROADMAP.md`.

## License

MIT

## Author

**Chandra Xavier**

Built under **Thyana Labs**.
