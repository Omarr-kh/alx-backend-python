#!/usr/bin/env python3
""" unittests for utils.access_nested_map """
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import *
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


class TestGetJson(unittest.TestCase):
    """ unittests for getJson method """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
    ) -> None:
        """ test get_json's output. """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)
