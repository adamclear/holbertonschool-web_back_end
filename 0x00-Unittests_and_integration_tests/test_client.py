#!/usr/bin/env python3
''' Unittests for client '''


from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest import mock, TestCase
from unittest.mock import MagicMock, patch, PropertyMock


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

    def test_public_repos_url(self):
        ''' public_repos_url tests '''
        with patch("client.get_json",
                   new_callable=PropertyMock,
                   return_value={"repos_url": "url"}):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "url")

    @patch("client.get_json")
    def test_public_repos(self, mockJson):
        ''' public_repos tests '''
        with patch("client.GithubOrgClient.public_repos",
                   new_callable=PropertyMock) as mockRepo:
            goc = GithubOrgClient("org_name")
            mockJson.return_value = {"repos_url": "url"}
            mockRepo.return_value = goc.org.get("repos_url")
            self.assertEqual(goc.public_repos, "url")
            mockJson.assert_called_once()
            mockRepo.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        ''' has_license tests '''
        goc = GithubOrgClient("org_name")
        self.assertEqual(goc.has_license(repo, license_key), expected)
