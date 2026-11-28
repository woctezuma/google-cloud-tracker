import unittest
from unittest import mock

import requests

from src.discord_utils import post_message_to_discord


class TestPostMessageToDiscord(unittest.TestCase):
    def test_returns_none_without_webhook(self) -> None:
        self.assertIsNone(post_message_to_discord("hello", None))

    def test_returns_none_with_empty_message(self) -> None:
        self.assertIsNone(post_message_to_discord("", "123/abc"))

    def test_posts_message_and_checks_status(self) -> None:
        response = mock.Mock()
        with mock.patch(
            "src.discord_utils.requests.post",
            return_value=response,
        ) as post:
            result = post_message_to_discord("hello", "123/abc")

        self.assertIs(result, response)
        post.assert_called_once()
        response.raise_for_status.assert_called_once_with()

    def test_raises_on_http_error(self) -> None:
        response = mock.Mock()
        response.raise_for_status.side_effect = requests.HTTPError("400")
        with (
            mock.patch("src.discord_utils.requests.post", return_value=response),
            self.assertRaises(requests.HTTPError),
        ):
            post_message_to_discord("hello", "123/abc")


if __name__ == "__main__":
    unittest.main()
