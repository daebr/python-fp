from fp.applicative import Applicative


class Monad(Applicative):
    """
    A monad is a functor that provides an additional binding function that
    itself returns a monad. Like the applicative it sequences operations.
    """

    def bind(self, f):
        """
        Sequentially compose two actions by passing the value of the first
        `m a` into the second monadic-producing function `a -> m b` which
        produces the result `m b`.

        (m a, a -> m b) -> m b
        """
        pass
