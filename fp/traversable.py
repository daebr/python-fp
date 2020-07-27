from fp.foldable import Foldable
from fp.functor import Functor


class Traversable(Functor, Foldable):

    def sequence(self, pure):
        """Applicative f => (t (f a), a -> f a) -> f (t a)"""
        pass

    def traverse(self, pure, f):
        """Applicative f => (t a, a -> f a, a -> f b) -> f (t b)"""
        return self.map(f).sequence(pure)
