from dataclasses import dataclass, field
from typing import override

import numpy as np

from geoapp.model.mesurable import Mesurable2D
from geoapp.model.point import Point
from geoapp.model.shape import Shape


@dataclass(kw_only=True)
class Polygon(Shape, Mesurable2D):
    # TODO: validate len(vertices) >= 3 with a validator
    vertices: list[Point] = field(default_factory=list)

    @override
    def translate(self, delta_x: np.float64, delta_y: np.float64) -> None:
        for v in self.vertices:
            v.translate(delta_x, delta_y)

    @override
    def perimeter(self) -> float:
        # TODO
        return 1.0

    @override
    def area(self) -> float:
        # TODO: use Shoelace formula
        return 1.0
