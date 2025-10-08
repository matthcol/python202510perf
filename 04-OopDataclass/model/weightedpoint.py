from dataclasses import dataclass
from typing import override

from model.point import Point


@dataclass(kw_only=True)
class WeightedPoint(Point):
    weight: float = 1.0

    @override
    def __str__(self) -> str:
        return f"{super().__str__()}!{self.weight:0.3f}"

    # @override    
    # def dummy(self):
    #     print("dummy from WeightedPoint")
