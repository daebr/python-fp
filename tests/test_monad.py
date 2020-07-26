import unittest
import context
from exactly_one import ExactlyOne

class TestMonad(unittest.TestCase):

    def test_left_identity_law(self):
        pure = ExactlyOne
        add1M = lambda x : pure(x + 1)
        self.assertEqual(
            pure(1).bind(add1M),
            add1M(1)
        )

    def test_right_identity_law(self):
        pure = ExactlyOne
        self.assertEqual(
            pure(1).bind(pure),
            pure(1)
        )

    def test_associativity_law(self):
        pure = ExactlyOne
        add1M = lambda x : pure(x + 1)
        doubleM = lambda x : pure(x * 2)
        self.assertEqual(
            pure(1).bind(add1M).bind(doubleM),
            pure(1).bind(lambda x : add1M(x).bind(doubleM))
        )

if __name__ == '__main__':
    unittest.main()