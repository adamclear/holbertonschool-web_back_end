#!/usr/bin/env python3
''' Unittests for client '''


from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest import mock, TestCase
from unittest.mock import MagicMock, patch


class TestGithubOrgClient(TestCase):
    ''' Tests for GithubOrgClient '''
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json",
           MagicMock(return_value={"key": "value"}))
    def test_org(self, org_name: str) -> None:
        ''' org tests '''
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"key": "value"})
