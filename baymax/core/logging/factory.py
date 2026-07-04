"""
Structured logging factory for Baymax OS.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import structlog


def configure_logging(
    level: str = "INFO",
    log_directory: Path | None = None,
    json_logging: bool = True,
) -> structlog.stdlib.BoundLogger:
    """
    Configure structured logging for Baymax OS.

    Runtime and services use structlog loggers with stable event names and
    key-value fields. A file handler is added when ``log_directory`` is
    supplied by configuration.
    """

    resolved_level = _resolve_level(level)
    handlers: list[logging.Handler] = [logging.StreamHandler(sys.stdout)]

    if log_directory is not None:
        log_directory.mkdir(parents=True, exist_ok=True)
        handlers.append(
            logging.FileHandler(
                log_directory / "baymax.log",
                encoding="utf-8",
            )
        )

    logging.basicConfig(
        format="%(message)s",
        handlers=handlers,
        level=resolved_level,
        force=True,
    )

    renderer = (
        structlog.processors.JSONRenderer()
        if json_logging
        else structlog.dev.ConsoleRenderer(colors=False)
    )

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            renderer,
        ],
        wrapper_class=structlog.make_filtering_bound_logger(resolved_level),
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    return structlog.get_logger("baymax")


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """Return a named Baymax logger."""

    return structlog.get_logger(name)


def _resolve_level(level: str) -> int:
    """Return a logging level constant for a configuration value."""

    normalized_level = level.upper()
    resolved_level = getattr(logging, normalized_level, None)

    if not isinstance(resolved_level, int):
        raise ValueError(f"Unsupported logging level: {level}")

    return resolved_level
