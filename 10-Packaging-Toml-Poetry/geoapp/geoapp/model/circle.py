from dataclasses import dataclass, field
from typing import cast, override

import numpy as np

from geoapp.model.mesurable import Mesurable2D
from geoapp.model.point import Point
from geoapp.model.shape import Shape


@dataclass(kw_only=True)
class Circle(Shape, Mesurable2D):
    radius: np.float64 = np.float64(1.0)
    center: Point = field(default_factory=Point)

    @override  # from Shape
    def translate(self, delta_x: np.float64, delta_y: np.float64) -> None:
        raise NotImplementedError

    @override  # from Mesurable2D
    def perimeter(self) -> np.float64:
        return np.float64(2.0) * np.pi * self.radius

    @override  # from Mesurable2D
    def area(self) -> np.float64:
        return cast(np.float64, np.pi * self.radius**2)
