from fp.core import const


class Foldable:

    def fold(self, f, z):
        """(t a, ((a, b) -> b), b) -> b"""
        pass

    def length(self):
        """t a -> int"""
        return self.fold(lambda a, z: z + 1, 0)

    def isEmpty(self):
        """t a -> bool"""
        return self.fold(lambda a, b: False, True)

    def contains(self, a):
        """(t a, a) -> bool"""
        return self.fold(lambda av, z: z or av == a, False)
