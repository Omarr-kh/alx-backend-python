#!/usr/bin/env python3
""" type-annotated safe_first_element function """
from typing import Any, List, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safely returns first element of a sequence """
    if lst:
        return lst[0]
    else:
        return None
