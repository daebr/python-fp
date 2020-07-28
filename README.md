# FPy
FPy is a functional programming library for Python. It includes a number of types
and patterns from functional programming such as Functors, Monads and Foldable
structures.

## Core Principles
Several core principles are characterised by this library and it is important to
adhere to these principles in order to get the most out of this library.

### Non-mutating functions
Immutability is a building block of functional programming. Not having to worry
about mutating states makes programs easier to reason about. Although this
library doesn't provide immutable classes, their intent is not to mutate.

None of the provided functions in the library mutate any values and to get the
most out of this library that should be adhered to. For inevitable "side effects"
such as IO (files, databases, etc.) then leave them at the door. That is to keep
them at the boundaries of the application and leave the business logic as pure
functions (see referential transparency).

### Structural equality
Since none of the classes are mutated, it is important that they support
structural equality. When using types with this library they would also benefit
from implementing structural equality.

### Referential transparency
Pure functions are important in functional programming. For a function to be
pure it must always return the same output when given the same input. This
referential transparency means you could effectively replace function calls with
values and the application would operate the same way. This library is designed
to be utilised with pure functions.

### No `None` values
To avoid unexpected behaviour, None values should not be introduced into this
library. Instead there is the `Option` type which can be created from a potential
None value through the function `asOption`.

### Function composition and higher-order functions
This library supports writing functions that feed into and compose into other
functions. Many of the functions in this library accept functions as arguments
and even return functions as results (higher-order functions). Learn how to
combine them and feed them into each other to get the most out of this library.

## Disclaimer
I am new to Python and do not know the intracacies of Python performance. There
are functions and types here that may not perform well, in particular recursion
such as the `LinkedList` type and functions operating on it.

I enjoy functional programming and wanted to port some of the Haskell functions
and types across to Python as an experiment, learning experience and for fun. So
please enjoy but be warned that it may not be suitable for production code.
