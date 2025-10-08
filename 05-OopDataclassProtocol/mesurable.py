
from typing import Protocol, runtime_checkable


@runtime_checkable
class Mesurable1D(Protocol):
    """Protocol
    """
    
    def length(self) -> float: ...

@runtime_checkable # si on veut faire de la vérification dynamique
class Mesurable2D(Protocol):
    """Protocol
    """

    def perimeter(self) -> float: ...

    def area(self) -> float: ...

