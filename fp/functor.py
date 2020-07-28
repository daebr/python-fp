from fp.core import const


class Functor:
    """
    A functor is a container that provides a mapping operation which
    applies a function over its contents.
    """

    def map(self, f):
        """
        Change the contents of the functor by applying a mapping operation,
        changing it from a functor of type `a` (f a) into a functor of type `b`
        (f b). The structure of the functor is preserved.

        (f a, a -> b) -> f b
        """
        pass

    def replaceWith(self, a):
        """
        Replace the contents of the functor (f a) with a value b (f b). The
        structure of the functor is preserved.

        (f a, b) -> f b
        """
        return self.map(const(a))

    def void(self):
        """
        Replace the contents of the functor (f a) with a unit value (f ()). The
        structure of the functor is preserved.

        f a -> f ()
        """
        return self.replaceWith(())
