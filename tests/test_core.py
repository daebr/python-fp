import unittest
import context
from fp.core import *

class TestCore(unittest.TestCase):
    
    def test_id(self):
        assert identity(1) == 1

    def test_const(self):
        c1 = const(1)
        assert c1(2) == 1

    def test_andThen(self):
        f = lambda x : x + 1
        g = lambda x : x * 2
        fg = f |andThen| g
        self.assertEqual(fg(1), 4)

    def test_compose(self):
        f = lambda x : x + 1
        g = lambda x : x * 2
        fg = f |compose| g
        self.assertEqual(fg(1), 3)

    def test_curry(self):
        add = lambda x,y : x + y
        assert curry(add)(1)(2) == 3

if __name__ == '__main__':
    unittest.main()