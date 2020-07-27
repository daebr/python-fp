import unittest
from fp.linked_list import cons, nil, toLinkedList
from exactly_one import ExactlyOne


class TestTraversable(unittest.TestCase):

    def test_sequence(self):
        pure = ExactlyOne
        self.assertEqual(
            toLinkedList([pure(1), pure(2)]).sequence(pure),
            pure(toLinkedList([1, 2]))
        )

    def test_traverse(self):
        pure = ExactlyOne
        def f(x): return pure(x + 1)
        expected = pure(toLinkedList([2, 3]))
        actual = toLinkedList([1, 2]).traverse(pure, f)
        print(str(expected) + " == " + str(actual))
        self.assertEqual(
            toLinkedList([1, 2]).traverse(pure, f),
            pure(toLinkedList([2, 3]))
        )


if __name__ == '__main__':
    unittest.main()
