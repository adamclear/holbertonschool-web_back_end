#!/usr/bin/env python3
''' Unittests for utils '''


from parameterized import parameterized
import typing
from unittest import TestCase, mock
from utils import access_nested_map, get_json, memoize


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

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
        ({"a": {"b": 2}}, ("b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: dict,
                                         path: tuple) -> None:
        ''' access_nested_map exception test '''
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    ''' Tests for get_json '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self,
                      url: str,
                      payload: dict) -> None:
        ''' get_json test '''
        with mock.patch("requests.get") as getit:
            getit.return_value.json.return_value = payload
            self.assertEqual(get_json(url), payload)


class TestMemoize(TestCase):
    ''' Tests for memoize '''
    def test_memoize(self):
        ''' memoize test '''
        class TestClass:
            ''' Test class for memoize tests '''
            def a_method(self):
                ''' Test method for class '''
                return 42

            @memoize
            def a_property(self):
                ''' Test property for class '''
                return self.a_method()

        with mock.patch.object(TestClass,
                               'a_method',
                               return_value=42) as mockingbird:
            mockObj = TestClass()
            self.assertEqual(mockObj.a_property, 42)
            self.assertEqual(mockObj.a_property, 42)
            mockingbird.assert_called_once()
