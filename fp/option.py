from fp.monad import Monad
from fp.traversable import Traversable


class Option(Monad, Traversable):
    """A type that represents some value (Some) or no value (Nothing).

    This type adheres to structural equality.
    """
    pass

    @staticmethod
    def pure(a):
        return Some(a)

    def isNone(self): pass

    def isSome(self): pass


class Nothing(Option):

    def __eq__(self, other):
        if isinstance(other, Nothing):
            return True
        else:
            return False

    def __str__(self):
        return "Nothing"

    def isNone(self):
        return True

    def isSome(self):
        return False

    def map(self, f):
        return Nothing()

    def ap(self, a):
        return Nothing()

    def bind(self, f):
        return Nothing()

    def fold(self, f, z):
        return z

    def sequence(self, pure):
        return pure(Nothing())


class Some(Option):
    def __init__(self, a):
        self.value = a

    def __eq__(self, other):
        if isinstance(other, Some):
            return self.value == other.value
        else:
            return False

    def __str__(self):
        return "Some (" + str(self.value) + ")"

    def isNone(self):
        return False

    def isSome(self):
        return True

    def map(self, f):
        return Some(f(self.value))

    def ap(self, a):
        if isinstance(a, Nothing):
            return Nothing()
        else:
            return Some(self.value(a.value))

    def bind(self, f):
        return f(self.value)

    def fold(self, f, z):
        return f(self.value, z)

    def sequence(self, pure):
        return self.value.map(some)


"""a -> Option a"""
some = Some

"""Option a"""
nothing = Nothing()


def asOption(obj):
    """Test any object for NoneType and convert to an option type.

    Object -> Option a
    """
    if obj is None:
        return nothing
    else:
        return some(obj)
