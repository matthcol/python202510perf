from dataclasses import dataclass
from typing import override

from geoapp.model.point import Point


@dataclass(kw_only=True)
class ColoredPoint(Point):
    color: str = "#000000"

    @override
    def __str__(self) -> str:
        return f"{super().__str__()}@{self.color}"

    @override
    def dummy(self):
        print("dummy from ColoredPoint")
