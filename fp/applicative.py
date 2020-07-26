from fp.core import *
from fp.functor import Functor

class Applicative(Functor):
    def pure(self, a):
        pass

    def ap(self, a):
        pass

    def replaceWithA(self, a):
        return self.replaceWith(identity).ap(a)