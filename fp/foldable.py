

class Foldable:
    """
    A foldable is a data structure that can be collapsed into a single value.
    """

    def fold(self, f, z):
        """
        Apply a two-parameter function `f` to each element of the foldable
        structure `t a`, passing the result onto the next element. An initial
        value `z` is required for the first element (or returned for an empty
        structure).

        (t a, ((a, b) -> b), b) -> b
        """
        pass

    def length(self):
        """
        Count the number of elements in the structure `t a`.

        t a -> int
        """
        return self.fold(lambda a, z: z + 1, 0)

    def isEmpty(self):
        """
        Check if the structure is empty.

        t a -> bool
        """
        return self.fold(lambda a, b: False, True)

    def contains(self, a):
        """
        Check if the structure contains a supplied value.

        (t a, a) -> bool
        """
        return self.fold(lambda av, z: z or av == a, False)
