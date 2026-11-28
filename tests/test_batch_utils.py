import unittest

from src.batch_utils import chunks


class TestChunks(unittest.TestCase):
    def test_even_split(self) -> None:
        self.assertEqual(list(chunks([1, 2, 3, 4], 2)), [[1, 2], [3, 4]])

    def test_uneven_split(self) -> None:
        self.assertEqual(list(chunks([1, 2, 3, 4, 5], 2)), [[1, 2], [3, 4], [5]])

    def test_empty_list(self) -> None:
        self.assertEqual(list(chunks([], 3)), [])


if __name__ == "__main__":
    unittest.main()
