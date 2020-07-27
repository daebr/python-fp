from fp.core import identity
from fp.functor import Functor


class Applicative(Functor):

    def pure(self, a):
        """(f b, a) -> f a"""
        pass

    def ap(self, a):
        """(f (a -> b), f a) -> f b"""
        pass

    def replaceWithA(self, a):
        """(f a, f b) -> f b"""
        return self.replaceWith(identity).ap(a)
