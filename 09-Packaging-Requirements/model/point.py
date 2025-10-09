"""module point
"""


from dataclasses import dataclass, field
import numpy as np
from typing import Self, cast, override

from model.shape import Shape
# from .shape import Shape


@dataclass(
    # slots=True, # fige la liste des attributs
    # frozen=True, # lecture seule (pas de setter)
    kw_only=True, 
    # order=True,
)
class Point(Shape):
    x: np.float64 = np.float64(0.0)
    y: np.float64 = np.float64(0.0)

    @override
    def __str__(self) -> str:
        return f"{super().__str__()}({self.x}, {self.y})"
    
    # autre: bool = field(repr=False, default=False)
    # friends: list['Point'] = field(default_factory=list)

    # # equivalent généré par @dataclass
    # def __init__(self, x: float = 0.0, y: float = 0.0, autre: bool = False, friends: list['Point'] | None = None):
    #     self.friends: list['Point']
    #     if friends is None:
    #         self.friends = []
    #     else:
    #         self.friends = friends 

    @override
    def translate(self, delta_x: np.float64, delta_y: np.float64) -> None:
        self.x += delta_x
        self.y += delta_y

    def distance(self, other: 'Point') -> np.float64:
        p1 = np.array(self.x, self.y)
        p2 = np.array(other.x, other.y)
        result = np.linalg.norm(p1 - p2)
        return cast(np.float64, result)
    
    def dummy(self):
        print("dummy from Point")

    # méthodes de classes:
    # - solution 1: @staticmethod (pas de meta programmation et d'adaptation 
    #      à la classe réelle en cas d'héritage)
    # - solution 2: @classmethod (adaptation à la classe réelle en cas d'héritage)
    #      utile pour créer des instances avec type adaptatif

    # @staticmethod
    # def from_coords(x: float, y: float) -> 'Point':
    #     return Point(x=x, y=y)


    @classmethod
    def from_coords(cls, x: np.float64, y: np.float64) -> Self:
        return cls(x=x, y=y)




