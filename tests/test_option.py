import unittest
import context
from fp.core import identity, curry, andThen, composeRight
from fp.option import Nothing, some, nothing
from fp.linked_list import LinkedList
from fp.linked_list import toLinkedList


class TestOption(unittest.TestCase):

    def test_eq_nothing(self):
        self.assertEqual(Nothing(), Nothing())

    def test_eq_some(self):
        self.assertEqual(some(1), some(1))
        self.assertNotEqual(some(0), some(1))

    def test_isNone(self):
        self.assertTrue(nothing.isNone())
        self.assertFalse(some(1).isNone())

    def test_isSome(self):
        self.assertFalse(nothing.isSome())
        self.assertTrue(some(1).isSome())

    def test_functor_identity_law(self):
        a = some(1)
        self.assertEqual(
            identity(a),
            a.map(identity)
        )
        self.assertEqual(
            identity(nothing),
            nothing.map(identity)
        )

    def test_functor_associativity_law(self):
        a = some(1)
        def f(x): return x + 1
        def g(x): return x * 2
        self.assertEqual(
            a.map(f).map(g),
            a.map(f |andThen| g)
        )

    def test_map(self):
        def f(x): return x + 1
        self.assertEqual(
            some(1).map(f),
            some(2)
        )
        self.assertEqual(
            nothing.map(f),
            nothing
        )

    def test_applicative_identity_law(self):
        pure = some
        self.assertEqual(
            pure(identity).ap(pure(1)),
            pure(1)
        )

    def test_applicative_homomorphism_law(self):
        pure = some
        def add1(x): return x + 1
        self.assertEqual(
            pure(add1).ap(pure(2)),
            pure(add1(2))
        )

    def test_applicative_interchange_law(self):
        pure = some
        def funcApp(a): return lambda f: f(a)
        def add1(x): return x + 1
        self.assertEqual(
            pure(add1).ap(pure(2)),
            pure(funcApp(2)).ap(pure(add1))
        )

    def test_applicative_composition_law(self):
        pure = some
        def add1(x): return x + 1
        def double(x): return x * 2
        f = curry(composeRight)
        self.assertEqual(
            pure(f).ap(pure(add1)).ap(pure(double)).ap(pure(1)),
            pure(add1).ap(pure(double).ap(pure(1)))
        )

    def test_ap(self):
        def add(x): return lambda y: x + y
        self.assertEqual(
            some(add).ap(some(1)).ap(some(2)),
            some(3)
        )
        self.assertEqual(
            some(add).ap(nothing).ap(some(2)),
            nothing
        )

    def test_monad_left_identity_law(self):
        pure = some
        def add1M(x): return pure(x + 1)
        self.assertEqual(
            pure(1).bind(add1M),
            add1M(1)
        )

    def test_monad_right_identity_law(self):
        pure = some
        self.assertEqual(
            pure(1).bind(pure),
            pure(1)
        )

    def test_monad_associativity_law(self):
        pure = some
        def add1M(x): return pure(x + 1)
        def doubleM(x): return pure(x * 2)
        self.assertEqual(
            pure(1).bind(add1M).bind(doubleM),
            pure(1).bind(lambda x: add1M(x).bind(doubleM))
        )

    def test_bind(self):
        def add1M(x): return some(x + 1)
        self.assertEqual(
            some(2).bind(add1M),
            some(3)
        )
        self.assertEqual(
            nothing.bind(add1M),
            nothing
        )

    def test_fold(self):
        def toStr(a, z): return str(a) + ", " + z
        self.assertEqual(
            some(1).fold(toStr, "0"),
            "1, 0"
        )
        self.assertEqual(
            nothing.fold(toStr, "0"),
            "0"
        )

    def test_sequence_some(self):
        option = some(toLinkedList([1, 2, 3]))
        xs = toLinkedList([some(1), some(2), some(3)])
        self.assertEqual(option.sequence(LinkedList.pure), xs)
        self.assertEqual(xs.sequence(some), option)

    def test_sequence_nothing(self):
        self.assertEqual(
            nothing.sequence(LinkedList.pure),
            toLinkedList([nothing])
        )
        self.assertEqual(
            toLinkedList([some(1), nothing, some(3)]).sequence(some),
            nothing
        )
