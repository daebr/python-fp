from fp.foldable import Foldable
from fp.functor import Functor


class Traversable(Functor, Foldable):
    """
    A traversable is a foldable structure that allows the inversion of
    the applicative functor contained inside.

    For example it will allow the conversion of a list of options into
    an option of list.
    """

    def sequence(self, pure):
        """
        Take a traversable structure of applicative functors and return
        an applicative functor of the traversable structure. The pure
        function from the applicative is needed to support some sequences.

        Applicative f => (t (f a), a -> f a) -> f (t a)
        """
        pass

    def traverse(self, pure, f):
        """
        Take a traversable structure and apply a function that maps each
        element to an applicative functor, then sequence the results so
        that the applicative wraps the traversable. The pure function
        of the applicative is required for some traversals.

        Applicative f => (t a, a -> f a, a -> f b) -> f (t b)
        """
        return self.map(f).sequence(pure)
