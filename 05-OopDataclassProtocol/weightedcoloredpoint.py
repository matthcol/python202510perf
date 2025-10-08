
from dataclasses import dataclass
from coloredpoint import ColoredPoint
from weightedpoint import WeightedPoint

@dataclass(kw_only=True)
class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    pass