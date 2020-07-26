import unittest
from exactly_one import ExactlyOne


class TestFoldable(unittest.TestCase):

    def test_fold(self):
        def add(x, y): return x + y
        self.assertEqual(
            ExactlyOne(2).fold(add, 1),
            3
        )


if __name__ == '__main__':
    unittest.main()
