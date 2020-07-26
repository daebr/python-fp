from functools import partial

class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

identity = lambda a : a
const = lambda a : lambda b : a

def curry(f):
    return lambda a : lambda b : f(a,b)

@Infix
def andThen(f, g):
    return lambda a : g(f(a))

@Infix
def compose(f, g):
    return lambda a : f(g(a))

composeLeft = lambda f : lambda g : lambda a : g(f(a))
composeRight = lambda f : lambda g : lambda a : f(g(a))