from fp.core import const


class Functor:

    def map(self, f):
        """(f a, a -> b) -> f b"""
        pass

    def replaceWith(self, a):
        """(f a, b) -> f b"""
        return self.map(const(a))

    def void(self):
        """f a -> f ()"""
        return self.replaceWith(())
