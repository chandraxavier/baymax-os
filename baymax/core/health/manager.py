"""
Health manager for Baymax OS.
"""

from __future__ import annotations

from baymax.core.health.models import HealthReport, HealthStatus


class HealthManager:
    """Collects and stores health reports from managed services."""

    def __init__(self) -> None:
        self._reports: dict[str, HealthReport] = {}

    def record(self, report: HealthReport) -> None:
        """Store the latest health report for a service."""

        self._reports[report.service] = report

    def get(self, service_name: str) -> HealthReport | None:
        """Return the latest report for a service."""

        return self._reports.get(service_name)

    def all(self) -> tuple[HealthReport, ...]:
        """Return all known health reports."""

        return tuple(self._reports.values())

    def aggregate_status(self) -> HealthStatus:
        """Return the aggregate runtime health status."""

        if not self._reports:
            return HealthStatus.UNKNOWN

        statuses = {report.status for report in self._reports.values()}

        if HealthStatus.UNHEALTHY in statuses:
            return HealthStatus.UNHEALTHY

        if HealthStatus.DEGRADED in statuses:
            return HealthStatus.DEGRADED

        if HealthStatus.WARNING in statuses:
            return HealthStatus.WARNING

        return HealthStatus.HEALTHY
