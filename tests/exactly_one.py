import context
from fp.monad import Monad
from fp.traversable import Traversable


class ExactlyOne(Monad, Traversable):
    def __init__(self, a):
        self.value = a

    def map(self, f):
        return ExactlyOne(f(self.value))

    def pure(self, a):
        return ExactlyOne(a)

    def ap(self, a):
        return ExactlyOne(self.value(a.value))

    def bind(self, f):
        return f(self.value)

    def fold(self, f, z):
        return f(self.value, z)

    def sequence(self, p):
        p(self.pure).ap(self.value)

    def __eq__(self, other):
        if isinstance(other, ExactlyOne):
            return self.value == other.value
        return False
