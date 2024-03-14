#!/usr/bin/env python3
""" type-annotated to_kv function """
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """ returns a tuple """
    return (k, float(v**2))
