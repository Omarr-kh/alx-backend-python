#!/usr/bin/env python3
""" type-annotated make_multiplier function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function """
    return lambda x: x * multiplier
