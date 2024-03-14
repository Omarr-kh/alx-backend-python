#!/usr/bin/env python3
""" type-annotated sum of list function """


def sum_list(input_list: list[float]) -> float:
    """ returns sum of list elements """
    return float(sum(input_list))
