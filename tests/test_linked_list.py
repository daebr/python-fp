import unittest
import context
from fp.core import *
from fp.linked_list import *

class TestLinkedList(unittest.TestCase):

    def test_eq_nil(self):
        self.assertEqual(nil, nil)

    def test_eq_cons(self):
        self.assertEqual(
            cons(1, cons(2, cons(3, nil))),
            toLinkedList([1,2,3])
        )

    def test_functor_identity_law(self):
        l = toLinkedList([1,2,3])
        self.assertEqual(
            identity(l),
            l.map(identity)
        )

    def test_functor_associativity_law(self):
        l = toLinkedList([1,2,3])
        f = lambda x : x + 1
        g = lambda x : x * 2
        self.assertEqual(
            l.map(f).map(g),
            l.map(f |andThen| g)
        )

    def test_fold(self):
        add = lambda x, y : x + y
        self.assertEqual(
            toLinkedList([1,2,3]).fold(add, 0),
            6
        )

if __name__ == '__main__':
    unittest.main()