# module point

from typing import Self, overload, override


class Point: # hérite auto de la classe object
    """ Represents a 2D point with its coordinates x, y

        Example:

            p = Point(3.5, 5.0)
    """

    # __slots__ = ["x", "y"]

    # constructeur
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # surcharge de builtins:
    # par défaut: str, repr, bool

    # overrides both repr (and str if not implemented)
    @override # since 3.12
    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"
    
    @override
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    # surcharge d'opérateurs
    # * par défaut: ==, != (basées sur l'@ mémoire)
    # * liste correspondance: https://docs.python.org/3/library/operator.html

    @override
    def __eq__(self, other: object) -> bool:
        # optimisation
        if self is other:
            return True
        
        # sol 1: autre est au moins 1 Point (autre est 1 Point ou objet + spécialisé)
        if not isinstance(other, Point):
            return NotImplemented
       
        # sol2: strict
        # if type(other) is not Point:
        #     return NotImplemented
        return (self.x ,self.y) == (other.x, other.y)


    # TODO: addition avec 1 point, 1 scalaire, 1 tuple

    @overload
    def __add__(self, other: 'Point') -> Self:...

    @overload
    def __add__(self, other: float) -> Self:...

    @overload
    def __add__(self, other: tuple[float, float]) -> Self:...

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(x=self.x + other.x, y=self.y + other.y)
        elif isinstance(other, float):
            return Point(x=self.x + other, y=self.y + other)
        elif isinstance(other, tuple) and len(other) == 2:
            x, y = other
            if not isinstance(x, float) or not isinstance(y, float):
                return NotImplemented
            return Point(x=self.x + x, y=self.y + y)
        else:
            return NotImplemented

    @overload
    def __radd__(self, other: 'Point') -> Self:...

    @overload
    def __radd__(self, other: float) -> Self:...

    @overload
    def __radd__(self, other: tuple[float, float]) -> Self:...

    def __radd__(self, other):
        return self.__add__(other)

    @overload
    def __iadd__(self, other: 'Point') -> Self:...

    @overload
    def __iadd__(self, other: float) -> Self:...

    @overload
    def __iadd__(self, other: tuple[float, float]) -> Self:...


    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, float):
            self.x += other
            self.y += other
        elif isinstance(other, tuple) and len(other) == 2:
            x, y = other
            if not isinstance(x, float) or not isinstance(y, float):
                return NotImplemented
            self.x += x
            self.y += y
        else:
            return NotImplemented
        return self

if __name__ == '__main__':
    p1 = Point(3.5, 4.5)    # calls __new__ then __init__
    p2 = Point(x=7.5, y=1.5)
    for p in p1, p2:
        print(p.x, p.y)
        print(p) # calls str() => __str__
        print(repr(p)) # => __repr__
        print()
