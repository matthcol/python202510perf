
from dataclasses import dataclass
from coloredpoint import ColoredPoint
from weightedpoint import WeightedPoint

@dataclass
class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    pass