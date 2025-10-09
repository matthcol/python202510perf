from abc import ABC, abstractmethod

import numpy as np


class Mesurable1D(ABC):
    """Interface"""

    @abstractmethod
    def length(self) -> np.float64: ...


class Mesurable2D(ABC):
    """Interface"""

    @abstractmethod
    def perimeter(self) -> np.float64: ...

    @abstractmethod
    def area(self) -> np.float64: ...
