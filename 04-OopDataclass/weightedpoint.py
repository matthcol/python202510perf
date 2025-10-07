from dataclasses import dataclass

from point import Point


@dataclass(kw_only=True)
class WeightedPoint(Point):
    weight: float = 1.0