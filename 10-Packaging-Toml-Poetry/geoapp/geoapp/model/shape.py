from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override

import numpy as np


@dataclass(kw_only=True)
class Shape(ABC):  # ou ABCMeta
    """represents geometric shape"""

    name: str | None = None

    @override
    def __str__(self):
        return "?" if self.name is None else self.name

    @abstractmethod
    def translate(self, delta_x: np.float64, delta_y: np.float64) -> None:
        """
        translate this shape
        """
        ...
