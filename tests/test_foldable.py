import unittest
from exactly_one import ExactlyOne


class TestFoldable(unittest.TestCase):

    def test_fold(self):
        def add(x, y): return x + y
        self.assertEqual(
            ExactlyOne(2).fold(add, 1),
            3
        )

    def test_length(self):
        self.assertEqual(
            ExactlyOne(0).length(),
            1
        )

    def test_isEmpty(self):
        self.assertFalse(ExactlyOne(0).isEmpty())

    def test_contains(self):
        self.assertEqual(ExactlyOne(0).contains(1), False)
        self.assertEqual(ExactlyOne(1).contains(1), True)


if __name__ == '__main__':
    unittest.main()
