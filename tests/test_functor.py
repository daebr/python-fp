import unittest
import context
from fp.core import *
from exactly_one import ExactlyOne

class TestFunctor(unittest.TestCase):

    def test_identity_law(self):
        a = ExactlyOne(1)
        self.assertEqual(
            identity(a),
            a.map(identity)
        )

    def test_associativity_law(self):
        a = ExactlyOne(1)
        f = lambda x : x + 1
        g = lambda x : x * 2
        self.assertEqual(
            a.map(f).map(g),
            a.map(f |andThen| g)
        )

    def test_replaceWith(self):
        assert ExactlyOne(1).replaceWith(2) == ExactlyOne(2)

    def test_void(self):
        assert ExactlyOne(1).void() == ExactlyOne(())

if __name__ == '__main__':
    unittest.main()