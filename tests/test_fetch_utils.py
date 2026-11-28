import unittest
from unittest import mock

import requests

from src.fetch_utils import fetch_page, get_url


class TestGetUrl(unittest.TestCase):
    def test_without_token(self) -> None:
        self.assertNotIn("pageToken", get_url())

    def test_with_token(self) -> None:
        self.assertIn("pageToken=abc", get_url("abc"))


class TestFetchPage(unittest.TestCase):
    def test_returns_items_and_next_page_token(self) -> None:
        response = mock.Mock()
        response.json.return_value = {
            "items": [{"name": "a"}],
            "nextPageToken": "tok",
        }
        with mock.patch("src.fetch_utils.requests.get", return_value=response) as get:
            page_objects, token = fetch_page()

        self.assertEqual(page_objects, [{"name": "a"}])
        self.assertEqual(token, "tok")
        get.assert_called_once()
        response.raise_for_status.assert_called_once_with()

    def test_raises_on_http_error(self) -> None:
        response = mock.Mock()
        response.raise_for_status.side_effect = requests.HTTPError("500")
        with (
            mock.patch("src.fetch_utils.requests.get", return_value=response),
            self.assertRaises(requests.HTTPError),
        ):
            fetch_page()


if __name__ == "__main__":
    unittest.main()
