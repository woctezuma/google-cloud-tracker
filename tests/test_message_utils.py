import unittest

from src import message_utils
from src.constants import HASH_FIELD, TIME_FIELD
from src.message_utils import (
    CONTENT_FIELD,
    NAME_FIELD,
    SIZE_FIELD,
    object_batch_to_message,
    object_to_message,
)


def make_object() -> dict[str, str]:
    return {
        NAME_FIELD: "file.txt",
        TIME_FIELD: "2024-01-02T03:04:05.000Z",
        CONTENT_FIELD: "text/plain",
        SIZE_FIELD: "123",
        HASH_FIELD: "abc123",
    }


class TestObjectToMessage(unittest.TestCase):
    def test_contains_url_and_fields(self) -> None:
        message = object_to_message(make_object())

        self.assertIn(f"URL: {message_utils.DISPLAY_URL}file.txt", message)
        self.assertIn("Created at: 2024-01-02T03:04", message)
        self.assertIn("Content-Type: text/plain", message)
        self.assertIn("Size: 123 bytes", message)
        self.assertIn("Hash: abc123", message)


class TestObjectBatchToMessage(unittest.TestCase):
    def test_joins_one_message_per_object(self) -> None:
        message = object_batch_to_message([make_object(), make_object()])

        self.assertEqual(message.count("URL: "), 2)


if __name__ == "__main__":
    unittest.main()
