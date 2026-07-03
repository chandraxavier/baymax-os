# Baymax Logging

The logging package provides the core logging foundation for Baymax OS.

## Responsibilities

- Configure the `baymax` root logger.
- Add a service field to every Baymax log record.
- Write logs to stderr during development and boot.
- Optionally write logs to `baymax.log` in the configured log directory.

## Runtime Integration

The Runtime Engine configures logging after configuration has been loaded. The
boot banner is the only runtime output that uses `print()` before logging is
available.

## Service Rule

Services use the logger provided through `RuntimeContext`. Services do not
create independent logging systems or print directly to stdout.
