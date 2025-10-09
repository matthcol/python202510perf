from dataclasses import dataclass

from geoapp.model.coloredpoint import ColoredPoint
from geoapp.model.weightedpoint import WeightedPoint


@dataclass(kw_only=True)
class WeightedColoredPoint(WeightedPoint, ColoredPoint):
    pass

    # __str__: cumul du WeightedPoint.__str__ et ColoredPoint.__str__
    # Ex:  H(0.0, 0.0)@red!25.500
    # Explication: algo MRO
    #    - WeightedColoredPoint: pas de méthode
    #    - WeightedPoint: __str_ : f"{super().__str__()}!{self.weight:0.3f}"
    #        => super().__str__() va faire appel à celui de Colored
    #        => super().__str__() va faire appel à celui de Point
    #        => super().__str__() va faire appel à celui de Shape

    # @override
    # def __str__(self) -> str:
    #     # choix explicite de version parente
    #     return Point.__str__(self)

    # @override
    # def dummy(self):
    #     print("dummy from WeightedColoredPoint")
