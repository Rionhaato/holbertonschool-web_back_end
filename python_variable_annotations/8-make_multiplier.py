#!/usr/bin/env python3
"""Define a typed multiplier factory."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""

    def multiply(value: float) -> float:
        """Multiply a float by the enclosing multiplier."""
        return value * multiplier

    return multiply
