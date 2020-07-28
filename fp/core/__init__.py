from functools import partial


class Infix(object):
    """
    Use this class to define infix operators.

    Example:
    isa = Infix(lambda x,y: x.__class__ == y.__class__)

    [1,2,3] |isa| []
    [1,2,3] <<isa>> []
    """

    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        return self.func(other)

    def __ror__(self, other):
        return Infix(partial(self.func, other))

    def __call__(self, v1, v2):
        return self.func(v1, v2)


def identity(a):
    """
    The identity function. A function that returns its parameter.

    a -> a
    """
    return a


def const(a):
    """
    The constant function. A function that returns a constant value.

    a -> b -> a
    """
    return lambda b: a


def curry(f):
    """
    Convert a two-parameter function into two one-parameter functions. Curried
    functions will allow the partial application of arguments to form new
    functions.

    ((a, b) -> c) -> a -> b -> c
    """
    return lambda a: lambda b: f(a, b)


@Infix
def andThen(f, g):
    """
    Left to right function composition.

    (a -> b, b -> c) -> a -> c
    """
    return lambda a: g(f(a))


@Infix
def compose(f, g):
    """
    Right to left function composition.

    (b -> c, a -> b) -> a -> c
    """
    return lambda a: f(g(a))


def composeLeft(f, g):
    """
    Left to right function composition.

    (a -> b, b -> c) -> a -> c
    """
    return lambda a: g(f(a))


def composeRight(f, g):
    """
    Right to left function composition.

    (b -> c, a -> b) -> a -> c
    """
    return lambda a: f(g(a))
