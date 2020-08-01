import unittest
import context
from fp.core import identity, curry, andThen, composeRight
from fp.linked_list import Nil, cons, nil, toLinkedList
from exactly_one import ExactlyOne


class TestLinkedList(unittest.TestCase):

    def test_eq_nil(self):
        self.assertEqual(Nil(), Nil())

    def test_eq_cons(self):
        self.assertEqual(
            cons(1, cons(2, cons(3, nil))),
            toLinkedList([1, 2, 3])
        )

    def test_functor_identity_law(self):
        xs = toLinkedList([1, 2, 3])
        self.assertEqual(
            identity(xs),
            xs.map(identity)
        )

    def test_functor_associativity_law(self):
        xs = toLinkedList([1, 2, 3])
        def f(x): return x + 1
        def g(x): return x * 2
        self.assertEqual(
            xs.map(f).map(g),
            xs.map(f |andThen| g)
        )

    def test_map(self):
        xs = toLinkedList([1, 2, 3])
        def f(x): return x * 2
        self.assertEqual(
            xs.map(f),
            toLinkedList([2, 4, 6])
        )

    def test_applicative_identity_law(self):
        def pure(a): return cons(a, nil)
        self.assertEqual(
            pure(identity).ap(pure(1)),
            pure(1)
        )

    def test_applicative_homomorphism_law(self):
        def pure(a): return cons(a, nil)
        def add1(x): return x + 1
        self.assertEqual(
            pure(add1).ap(pure(2)),
            pure(add1(2))
        )

    def test_applicative_interchange_law(self):
        def pure(a): return cons(a, nil)
        def funcApp(a): return lambda f: f(a)
        def add1(x): return x + 1
        self.assertEqual(
            pure(add1).ap(pure(2)),
            pure(funcApp(2)).ap(pure(add1))
        )

    def test_applicative_composition_law(self):
        def pure(a): return cons(a, nil)
        def add1(x): return x + 1
        def double(x): return x * 2
        f = curry(composeRight)
        self.assertEqual(
            pure(f).ap(pure(add1)).ap(pure(double)).ap(pure(1)),
            pure(add1).ap(pure(double).ap(pure(1)))
        )

    def test_ap(self):
        def f(x): return x + 1
        def g(x): return x * 2
        fs = toLinkedList([f, g])
        xs = toLinkedList([1, 2, 3])
        self.assertEqual(
            fs.ap(xs),
            toLinkedList([2, 3, 4, 2, 4, 6])
        )

    def test_monad_left_identity_law(self):
        def pure(a): return cons(a, nil)
        def add1M(x): return pure(x + 1)
        self.assertEqual(
            pure(1).bind(add1M),
            add1M(1)
        )

    def test_monad_right_identity_law(self):
        def pure(a): return cons(a, nil)
        self.assertEqual(
            pure(1).bind(pure),
            pure(1)
        )

    def test_monad_associativity_law(self):
        def pure(a): return cons(a, nil)
        def add1M(x): return pure(x + 1)
        def doubleM(x): return pure(x * 2)
        self.assertEqual(
            pure(1).bind(add1M).bind(doubleM),
            pure(1).bind(lambda x: add1M(x).bind(doubleM))
        )

    def test_bind(self):
        def f(x): return toLinkedList([x, x + 1])
        xs = toLinkedList([1, 2, 3])
        self.assertEqual(
            xs.bind(f),
            toLinkedList([1, 2, 2, 3, 3, 4])
        )

    def test_fold(self):
        def add(x, y): return x + y
        self.assertEqual(
            toLinkedList([1, 2, 3]).fold(add, 0),
            6
        )


if __name__ == '__main__':
    unittest.main()
