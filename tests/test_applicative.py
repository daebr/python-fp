import unittest
import context
from fp.core import identity, curry, composeRight
from exactly_one import ExactlyOne


class ApplicativeTest(unittest.TestCase):

    def test_identity_law(self):
        pure = ExactlyOne
        self.assertEqual(
            pure(identity).ap(ExactlyOne(1)),
            ExactlyOne(1)
        )

    def test_homomorphism_law(self):
        pure = ExactlyOne
        def add1(x): return x + 1
        self.assertEqual(
            pure(add1).ap(pure(2)),
            pure(add1(2))
        )

    def test_interchange_law(self):
        pure = ExactlyOne
        def funcApp(a): return lambda f: f(a)
        def add1(x): return x + 1
        self.assertEqual(
            pure(add1).ap(pure(2)),
            pure(funcApp(2)).ap(pure(add1))
        )

    def test_composition_law(self):
        pure = ExactlyOne
        def add1(x): return x + 1
        def double(x): return x * 2
        self.assertEqual(
            pure(curry(composeRight)).ap(pure(add1)).ap(pure(double)).ap(pure(1)),
            pure(add1).ap(pure(double).ap(pure(1)))
        )

    def test_replaceWithA(self):
        self.assertEqual(
            ExactlyOne(1).replaceWithA(ExactlyOne(2)).value,
            ExactlyOne(2).value
        )


if __name__ == '__main__':
    unittest.main()
