#!/usr/bin/env python3
"""Parameterize a unit test
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch

from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map utils methods
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)