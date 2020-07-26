from fp.foldable import Foldable
from fp.functor import Functor

class LinkedList(Functor, Foldable):
    def length(self):
        pass

class Nil(LinkedList):
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


nil = Nil()
cons = Cons

def toLinkedList(l):
    if len(l) == 0:
        return nil
    else:
        return cons(l[0], toLinkedList(l[1:]))
