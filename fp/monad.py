from fp.applicative import Applicative


class Monad(Applicative):

    def bind(self, f):
        """(m a, a -> m b) -> m b"""
        pass
