#!/usr/bin/env python3
""" type-annotated sum of list function """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns sum of list elements """
    return float(sum(input_list))
