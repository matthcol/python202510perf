"""module point"""

from dataclasses import dataclass
from typing import Self, override

import numpy as np

from geoapp.model.shape import Shape

# from .shape import Shape


@dataclass(
    # slots=True, # fige la liste des attributs
    # frozen=True, # lecture seule (pas de setter)
    kw_only=True,
    # order=True,
)
class Point(Shape):
    x: np.float64 = np.float64(0.0)
    y: np.float64 = np.float64(0.0)

    @override
    def __str__(self) -> str:
        return f"{super().__str__()}({self.x}, {self.y})"

    @override
    def translate(self, delta_x: np.float64, delta_y: np.float64) -> None:
        self.x += delta_x
        self.y += delta_y

    def distance(self, other: "Point") -> np.float64:
        return np.hypot(self.x - other.x, self.y - other.y).astype(np.float64)

    def dummy(self):
        print("dummy from Point")

    @classmethod
    def from_coords(cls, x: np.float64, y: np.float64) -> Self:
        return cls(x=x, y=y)
