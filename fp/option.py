from fp.linked_list import Cons, Nil, curry
from fp.monad import Monad
from fp.foldable import Foldable


class Option(Monad, Foldable):
    """A type that represents some value (Some) or no value (Nothing).

    This type adheres to structural equality.
    """
    pass

    @staticmethod
    def pure(a):
        return Some(a)

    @staticmethod
    def sequence(xs):
        """
        Traverse a list of options to convert it into an option of list.

        [Option a] -> Option [a]
        """
        if isinstance(xs, Nil):
            return Option.pure(Nil())
        else:
            return Option.pure(curry(Cons)) \
                .ap(xs.head) \
                .ap(Option.sequence(xs.tail))

    @staticmethod
    def traverse(f, xs):
        """
        Apply a function from an `a` to an `Option a` over a linked list, then
        invert the result.

        ((a -> Option b), [a]) -> Option [b]
        """
        return Option.sequence(xs.map(f))

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
