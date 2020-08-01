import context
from fp.monad import Monad
from fp.foldable import Foldable


class ExactlyOne(Monad, Foldable):
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

    def __eq__(self, other):
        if isinstance(other, ExactlyOne):
            return self.value == other.value
        return False

    def __str__(self):
        return "ExactlyOne(" + str(self.value) + ")"
