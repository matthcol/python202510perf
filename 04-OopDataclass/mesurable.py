from abc import ABC, abstractmethod


class Mesurable1D(ABC):
    
    @abstractmethod
    def length(self) -> float:
        ...

class Mesurable2D(ABC):
    @abstractmethod
    def perimeter(self) -> float:
        ...

    @abstractmethod
    def area(self) -> float:
        ...

