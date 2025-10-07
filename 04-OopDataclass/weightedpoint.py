from dataclasses import dataclass

from point import Point


@dataclass
class WeightedPoint(Point):
    weight: float = 1.0