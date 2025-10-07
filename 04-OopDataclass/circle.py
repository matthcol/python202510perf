from dataclasses import dataclass, field
from point import Point
from shape import Shape

@dataclass
class Circle(Shape):
    radius: float = 1.0
    center: Point = field(default_factory=Point)