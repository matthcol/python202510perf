

from dataclasses import dataclass
from point import Point

@dataclass
class ColoredPoint(Point):
    color: str = "#000000"