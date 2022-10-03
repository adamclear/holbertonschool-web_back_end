#!/usr/bin/env python3
''' Unittests for utils '''


from parameterized import parameterized
import typing
from unittest import TestCase
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    ''' Tests for access_nested_map '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: dict,
                               path: tuple,
                               expected: typing.Union[int, dict]) -> None:
        ''' access_nested_map test '''
        self.assertEqual(access_nested_map(nested_map, path), expected)
