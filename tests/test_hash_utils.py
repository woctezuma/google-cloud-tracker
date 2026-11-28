import tempfile
import unittest
from pathlib import Path
from unittest import mock

from src import hash_utils
from src.constants import HASH_FIELD, TIME_FIELD
from src.hash_utils import load_hashes, save_hashes, to_hashes


def make_object(name: str, created: str, crc: str) -> dict[str, str]:
    return {"name": name, TIME_FIELD: created, HASH_FIELD: crc}


class TestToHashes(unittest.TestCase):
    def test_maps_hash_to_creation_time(self) -> None:
        objects = [make_object("a", "2024-01-01T00:00:00.000Z", "hash-a")]
        self.assertEqual(to_hashes(objects), {"hash-a": "2024-01-01T00:00:00.000Z"})


class TestSaveAndLoadHashes(unittest.TestCase):
    def test_round_trip_preserves_hash_order(self) -> None:
        objects = [
            make_object("a", "2024-01-01T00:00:00.000Z", "hash-a"),
            make_object("b", "2024-01-02T00:00:00.000Z", "hash-b"),
        ]
        with tempfile.TemporaryDirectory() as tmp_dir:
            hash_fname = str(Path(tmp_dir) / "crc32c.txt")
            with (
                mock.patch.object(hash_utils, "HASH_FNAME", hash_fname),
                mock.patch.object(hash_utils, "DATA_FOLDER", f"{tmp_dir}/"),
            ):
                save_hashes(objects)
                loaded = load_hashes()

        self.assertEqual(list(loaded.keys()), ["hash-a", "hash-b"])


if __name__ == "__main__":
    unittest.main()
