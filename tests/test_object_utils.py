import unittest

from src.constants import HASH_FIELD, TIME_FIELD
from src.object_utils import find_new_objects, sort_objects


def make_object(name: str, created: str, crc: str) -> dict[str, str]:
    return {"name": name, TIME_FIELD: created, HASH_FIELD: crc}


class TestSortObjects(unittest.TestCase):
    def test_sorts_by_creation_time(self) -> None:
        objects = [
            make_object("b", "2024-01-02T00:00:00.000Z", "hash-b"),
            make_object("a", "2024-01-01T00:00:00.000Z", "hash-a"),
        ]
        sorted_objects = sort_objects(objects)
        self.assertEqual([obj["name"] for obj in sorted_objects], ["a", "b"])


class TestFindNewObjects(unittest.TestCase):
    def test_detects_new_objects_and_updates_hashes(self) -> None:
        objects = [
            make_object("a", "2024-01-01T00:00:00.000Z", "hash-a"),
            make_object("b", "2024-01-02T00:00:00.000Z", "hash-b"),
        ]
        hashes: dict[str, None] = {"hash-a": None}

        new_objects, updated_hashes = find_new_objects(objects, hashes)

        self.assertEqual([obj["name"] for obj in new_objects], ["b"])
        self.assertEqual(
            updated_hashes,
            {
                "hash-a": None,
                "hash-b": "2024-01-02T00:00:00.000Z",
            },
        )

    def test_no_new_objects(self) -> None:
        objects = [make_object("a", "2024-01-01T00:00:00.000Z", "hash-a")]
        hashes: dict[str, None] = {"hash-a": None}

        new_objects, _ = find_new_objects(objects, hashes)

        self.assertEqual(new_objects, [])


if __name__ == "__main__":
    unittest.main()
