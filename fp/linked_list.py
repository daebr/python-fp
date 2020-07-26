from fp.foldable import Foldable
from fp.functor import Functor


class LinkedList(Functor, Foldable):
    """A linked list is a recursive type. A linked list `[a]` contains a head
    of `a` and a tail of `[a]`. An empty linked list is Nil.

    This type adheres structural equality.
    """
    pass


class Nil(LinkedList):
    """An empty linked list"""

    def __init__(self):
        ()

    def __eq__(self, other):
        return isinstance(other, Nil)

    def map(self, f):
        return Nil()

    def fold(self, f, z):
        return z


class Cons(LinkedList):
    def __init__(self, h, t):
        self.head = h
        self.tail = t

    def __eq__(self, other):
        if isinstance(other, Cons):
            return self.head == other.head and self.tail == other.tail
        return False

    def map(self, f):
        return Cons(f(self.head), self.tail.map(f))

    def fold(self, f, z):
        return f(self.head, self.tail.fold(f, z))


# An empty linked list
nil = Nil()

# (a, LinkedList<a>) -> LinkedList<a>
cons = Cons


def toLinkedList(list):
    """[a] -> LinkedList<a>"""
    if len(list) == 0:
        return nil
    else:
        return cons(list[0], toLinkedList(list[1:]))
