#!/usr/bin/env python3
"""type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier and returns a function that multiplies a float by multiplier"""
    def get_multiplier(val: float) -> float:
        return float(multiplier * val)
    return get_multiplier
