from fp.foldable import Foldable


class Traversable(Foldable):

    def sequence(self, pure):
        """Applicative f => (t (f a), a -> f a) -> f (t a)"""
        pass
