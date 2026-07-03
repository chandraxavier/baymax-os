"""
Runtime lifecycle transition policy.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

from baymax.core.runtime.state import (
    RUNTIME_STATE_TRANSITIONS,
    RuntimeState,
)


class RuntimeTransitionError(RuntimeError):
    """Raised when an invalid runtime state transition is requested."""


@dataclass(frozen=True, slots=True)
class RuntimeTransition:
    """Single runtime lifecycle transition."""

    previous_state: RuntimeState
    new_state: RuntimeState
    changed_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class RuntimeLifecycle:
    """
    Owns Runtime Engine state transitions.

    Runtime state is intentionally isolated from boot orchestration so future
    recovery and watchdog policies can reuse the same transition rules.
    """

    def __init__(self) -> None:
        self._state = RuntimeState.CREATED
        self._history: list[RuntimeTransition] = []

    @property
    def state(self) -> RuntimeState:
        """Current runtime state."""

        return self._state

    @property
    def history(self) -> tuple[RuntimeTransition, ...]:
        """Immutable transition history."""

        return tuple(self._history)

    def transition_to(self, new_state: RuntimeState) -> None:
        """Transition to a new state if the transition is allowed."""

        allowed_states = RUNTIME_STATE_TRANSITIONS[self._state]

        if new_state not in allowed_states:
            raise RuntimeTransitionError(
                "Invalid runtime transition "
                f"{self._state.value} -> {new_state.value}."
            )

        transition = RuntimeTransition(
            previous_state=self._state,
            new_state=new_state,
        )
        self._state = new_state
        self._history.append(transition)
