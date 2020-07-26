import unittest
import context
from exactly_one import ExactlyOne

class TestTraversable(unittest.TestCase):

    def test_sequence(self):
        add = lambda x,y : x + y
        self.assertEqual(ExactlyOne(2).fold(add, 1), 3)

if __name__ == '__main__':
    unittest.main()