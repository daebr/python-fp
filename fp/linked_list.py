from fp.core import curry
from fp.foldable import Foldable
from fp.monad import Monad


class LinkedList(Monad, Foldable):
    """
    A linked list is a recursive type. A linked list `[a]` contains a head
    of `a` and a tail of `[a]`. An empty linked list is Nil.

    This type adheres to structural equality.
    """

    @staticmethod
    def pure(a):
        return Cons(a, Nil())

    def isEmpty(self):
        pass

    def concat(self, other):
        pass


class Nil(LinkedList):
    """An empty linked list"""

    def __init__(self):
        ()

    def __eq__(self, other):
        return isinstance(other, Nil)

    def __str__(self):
        return "Nil"

    def map(self, f):
        return Nil()

    def ap(self, a):
        return Nil()

    def bind(self, f):
        return Nil()

    def fold(self, f, z):
        return z

    def isEmpty(self):
        return True

    def concat(self, other):
        return other


class Cons(LinkedList):
    def __init__(self, h, t):
        self.head = h
        self.tail = t

    def __eq__(self, other):
        if isinstance(other, Cons):
            return self.head == other.head and self.tail == other.tail
        return False

    def __str__(self):
        def foldStr(a, b):
            if b == "":
                return str(a)
            else:
                return str(a) + ", " + b
        return "LinkedList [" + self.fold(foldStr, "") + "]"

    def map(self, f):
        return Cons(f(self.head), self.tail.map(f))

    def ap(self, a):
        if isinstance(a, Nil):
            return Nil()
        else:
            return Cons(
                self.head(a.head),
                a.tail.map(self.head).concat(self.tail.ap(a))
            )

    def bind(self, f):
        return f(self.head).concat(self.tail.bind(f))

    def fold(self, f, z):
        return f(self.head, self.tail.fold(f, z))

    def isEmpty(self):
        return False

    def concat(self, other):
        return Cons(self.head, self.tail.concat(other))


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
