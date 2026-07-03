"""
Baymax Guardian Runtime

Guardian is the runtime supervisor for Baymax OS.

Responsibilities:
- Boot orchestration
- Initialize platform services
- Start managed services
- Monitor system health
- Coordinate graceful shutdown

This is intentionally minimal for Sprint 1.
"""

from datetime import datetime

from .state_machine import GuardianState


class GuardianRuntime:
    """Baymax Guardian Runtime."""

    def __init__(self) -> None:
        self.state = GuardianState.BOOTING
        self.boot_time = datetime.now()

    def start(self) -> None:
        """Start the Guardian runtime."""

        print("=" * 60)
        print("Baymax OS")
        print("Guardian Runtime")
        print("=" * 60)

        self.transition(GuardianState.INITIALIZING)

        print("Loading configuration...")

        print("Initializing logging...")

        print("Initializing event bus...")

        print("Starting service manager...")

        print("Initializing connectivity...")

        self.transition(GuardianState.STARTING_DASHBOARD)

        print("Launching Guardian Console...")

        self.transition(GuardianState.RUNNING)

        print("")
        print("Guardian Runtime Started Successfully")
        print(f"Current State : {self.state.value}")

    def transition(self, new_state: GuardianState) -> None:
        """Transition Guardian to a new state."""

        print(f"[STATE] {self.state.value} -> {new_state.value}")
        self.state = new_state


if __name__ == "__main__":
    runtime = GuardianRuntime()
    runtime.start()
