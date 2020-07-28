from fp.core import identity
from fp.functor import Functor


class Applicative(Functor):
    """
    An applicative is a type of functor that sequences operations and combines
    their results.

    Usually an applicative comes with a `pure` function that "lifts" a value
    into the applicative `a -> f a`. It is up to the implementations to
    provide this function.
    """

    def ap(self, a):
        """
        Apply a lifted function `f (a -> b)` to `f a` turning it into `f b`.
        Multi-parameter functions can be curried, lifted and then the lifted
        arguments applied sequentially.

        (f (a -> b), f a) -> f b
        """
        pass

    def replaceWithA(self, a):
        """
        Sequence two applicatives, discarding the result of the first.

        (f a, f b) -> f b
        """
        return self.replaceWith(identity).ap(a)
