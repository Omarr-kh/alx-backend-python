#!/usr/bin/env python3
""" unittests for client """
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ unittests for org """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, res: Dict, mocked: MagicMock) -> None:
        """ Tests the org method. """
        mocked.return_value = MagicMock(return_value=res)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), res)
        mocked.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """ Tests for property """
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
        ) as org_mocked:
            org_mocked.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch('client.get_json')
    def test_public_repos(self, mocked_json):
        """ Tests for public_repos method """
        repos_names = ['alx-storage', 'alx-backend-python', 'alx-backend']
        repos_list = [{'name': name} for name in repos_names]

        mocked_json.return_value = repos_list

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_urls:
            mocked_urls.return_value = 'https://github.com/test'

            org_client = GithubOrgClient('test')
            test1 = org_client.public_repos()
            test2 = org_client.public_repos()

            mocked_json.assert_called_once()
            mocked_urls.assert_called_once()

            self.assertEqual(test1, test2)
            self.assertEqual(test1, repos_names)
