"""
Logging factory for Baymax OS core services.
"""

from __future__ import annotations

import logging
from pathlib import Path


LOG_FORMAT = (
    "%(asctime)s %(levelname)s [%(name)s] "
    "service=%(baymax_service)s %(message)s"
)


class BaymaxServiceFilter(logging.Filter):
    """Ensure all log records contain a service field."""

    def filter(self, record: logging.LogRecord) -> bool:
        if not hasattr(record, "baymax_service"):
            record.baymax_service = record.name
        return True


def configure_logging(
    level: str = "INFO",
    log_directory: Path | None = None,
) -> logging.Logger:
    """
    Configure the Baymax root logger.

    The logger writes structured, service-aware records to stderr by default.
    A file handler is added when ``log_directory`` is supplied.
    """

    root_logger = logging.getLogger("baymax")
    root_logger.setLevel(_resolve_level(level))
    root_logger.handlers.clear()
    root_logger.propagate = False

    formatter = logging.Formatter(LOG_FORMAT)
    service_filter = BaymaxServiceFilter()

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(service_filter)
    root_logger.addHandler(stream_handler)

    if log_directory is not None:
        log_directory.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(
            log_directory / "baymax.log",
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        file_handler.addFilter(service_filter)
        root_logger.addHandler(file_handler)

    return root_logger


def _resolve_level(level: str) -> int:
    """Return a logging level constant for a configuration value."""

    normalized_level = level.upper()
    resolved_level = getattr(logging, normalized_level, None)

    if not isinstance(resolved_level, int):
        raise ValueError(f"Unsupported logging level: {level}")

    return resolved_level
