"""
Baymax Guardian Health Model

Every Baymax service exposes its health using this model.

Guardian uses these health reports for:
- Boot validation
- Service supervision
- Recovery
- Guardian Console
- Diagnostics
"""

from baymax.core.health.models import HealthReport, HealthStatus

__all__ = ["HealthReport", "HealthStatus"]
