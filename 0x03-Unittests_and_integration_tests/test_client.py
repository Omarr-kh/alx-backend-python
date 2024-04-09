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
        org_client = GithubOrgClient(org)
        self.assertEqual(org_client.org(), res)
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

    @parameterized.expand([
        ({'license': {'key': "bsd"}}, "bsd", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """ unittests for license """
        org_client = GithubOrgClient("google")
        has_license = org_client.has_license(repo, key)
        self.assertEqual(has_license, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests """
    @classmethod
    def setUpClass(cls) -> None:
        """ fixtures setup class """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def mocked_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=mocked_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """ test public_repos method. """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """ test public_repos method with a license. """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """ Remove fixtures """
        cls.get_patcher.stop()
