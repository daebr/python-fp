from fp.core import *

class Functor:
    def map(self, f):
        pass

    def replaceWith(self, a):
        return self.map(const(a))

    def void(self):
        return self.replaceWith(())