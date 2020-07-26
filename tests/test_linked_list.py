import unittest
import context
from fp.core import identity, andThen
from fp.linked_list import cons, nil, toLinkedList


class TestLinkedList(unittest.TestCase):

    def test_eq_nil(self):
        self.assertEqual(nil, nil)

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

    def test_fold(self):
        def add(x, y): return x + y
        self.assertEqual(
            toLinkedList([1, 2, 3]).fold(add, 0),
            6
        )


if __name__ == '__main__':
    unittest.main()
