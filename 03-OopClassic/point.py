# module point


from typing import Any, override


class Point:
    """ Represents a 2D point with its coordinates x, y

        Example:

            p = Point(3.5, 5.0)
    """

    # constructeur
    def __init__(self, x, y):
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

    def __eq__(self, other: Any) -> bool:
        # optimisation
        if self is other:
            return True
        
        # sol 1: autre est au moins 1 Point (autre est 1 Point ou objet + spécialisé)
        if not isinstance(other, Point):
            return NotImplemented
       
        # sol2: strict
        # if type(other) is not Point:
        #     return False
        
        return (self.x ,self.y) == (other.x, other.y)




if __name__ == '__main__':
    p1 = Point(3.5, 4.5)    # calls __new__ then __init__
    p2 = Point(x=7.5, y=1.5)
    for p in p1, p2:
        print(p.x, p.y)
        print(p) # calls str() => __str__
        print(repr(p)) # => __repr__
        print()
