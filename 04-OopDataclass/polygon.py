from dataclasses import dataclass, field
from typing import override

from mesurable import Mesurable2D
from point import Point
from shape import Shape


@dataclass(kw_only=True)
class Polygon(Shape, Mesurable2D):

    # TODO: validate len(vertices) >= 3 with a validator
    vertices: list[Point] = field(default_factory=list)

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
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
