

from dataclasses import dataclass
from point import Point

@dataclass(kw_only=True)
class ColoredPoint(Point):
    color: str = "#000000"