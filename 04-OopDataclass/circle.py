from dataclasses import dataclass, field
import math
from typing import override
from mesurable import Mesurable2D
from point import Point
from shape import Shape

@dataclass(kw_only=True)
class Circle(Shape, Mesurable2D):
    radius: float = 1.0
    center: Point = field(default_factory=Point)

    @override # from Shape
    def translate(self, delta_x: float, delta_y: float) -> None:
        raise NotImplementedError

    @override # from Mesurable2D
    def perimeter(self) -> float:
        return 2.0 * math.pi * self.radius 

    @override # from Mesurable2D
    def area(self) -> float:
        return math.pi * self.radius**2


