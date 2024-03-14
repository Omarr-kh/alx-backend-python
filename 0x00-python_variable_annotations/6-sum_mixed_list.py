#!/usr/bin/env python3
""" type-annotated sum of mixed types list function """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns sum of list elements """
    return float(sum(mxd_lst))
