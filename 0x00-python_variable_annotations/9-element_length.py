#!/usr/bin/env python3
""" type-annotated element_length function """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns list of tuples """
    return [(i, len(i)) for i in lst]
