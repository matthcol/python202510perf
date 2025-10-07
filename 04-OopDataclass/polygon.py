from dataclasses import dataclass, field

from point import Point
from shape import Shape


@dataclass
class Polygon(Shape):

    # TODO: validate len(vertices) >= 3
    vertices: list[Point] = field(default_factory=list)