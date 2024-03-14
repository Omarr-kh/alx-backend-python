#!/usr/bin/env python3
""" type-annotated safe_first_element function """
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """ safely gets a key's value from a dict """

    if key in dct:
        return dct[key]
    else:
        return default
