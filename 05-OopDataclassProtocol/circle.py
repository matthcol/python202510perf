from dataclasses import dataclass, field
import math
from typing import override
from mesurable import Mesurable2D
from point import Point
from shape import Shape

@dataclass(kw_only=True)
class Circle(Shape):
    radius: float = 1.0
    center: Point = field(default_factory=Point)

    @override # from Shape
    def translate(self, delta_x: float, delta_y: float) -> None:
        raise NotImplementedError

    def perimeter(self) -> float:
        return 2.0 * math.pi * self.radius 

    def area(self) -> float:
        return math.pi * self.radius**2


