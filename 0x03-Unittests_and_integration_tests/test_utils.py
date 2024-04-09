#!/usr/bin/env python3
""" unittests for utils.access_nested_map """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """ unittests for access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            sequence: Tuple[str],
            expected: Union[Dict, int]
    ) -> None:
        """ testing the method with the parameterized tests """
        self.assertEqual(access_nested_map(nested_map, sequence), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            sequence: Tuple[str],
            expected: Exception
    ) -> None:
        """ testing the method with the parameterized tests """
        with self.assertRaises(expected):
            access_nested_map(nested_map, sequence)
