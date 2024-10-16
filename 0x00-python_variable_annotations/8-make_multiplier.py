#!/usr/bin/env python3
"""
Complex mtypes - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a func that multipys 'multiplier' by float
    """
    def product(num: float) -> float:
        return num * multiplier
    return product
