
from dataclasses import dataclass, field
import math
from typing import Self, override

from shape import Shape


@dataclass(
    # slots=True, # fige la liste des attributs
    # frozen=True, # lecture seule (pas de setter)
    kw_only=True, 
    # order=True,
)
class Point(Shape):
    x: float = 0.0
    y: float = 0.0

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
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y

    def distance(self, other: 'Point') -> float:
        return math.dist((self.x, self.y), (other.x, other.y))

    # méthodes de classes:
    # - solution 1: @staticmethod (pas de meta programmation et d'adaptation 
    #      à la classe réelle en cas d'héritage)
    # - solution 2: @classmethod (adaptation à la classe réelle en cas d'héritage)
    #      utile pour créer des instances avec type adaptatif

    # @staticmethod
    # def from_coords(x: float, y: float) -> 'Point':
    #     return Point(x=x, y=y)


    @classmethod
    def from_coords(cls, x: float, y: float) -> Self:
        return cls(x=x, y=y)





if __name__ == '__main__':
    pt1 = Point(x=12.5, y=45.5)
    pt2 = Point()
    pt3 = Point(name="A", x=15.5, y=49.5)
    assert pt1 == Point(x=12.5, y=45.5)

    points = [pt1, pt2, pt3]
    for pt in points:
        print(pt)

    
    # si order=True
    # assert pt2 < pt1
    # points = [pt1, pt2]
    # points.sort()
    # print(points)
    # pt2.x = 20.0
    # points.sort()
    # print(points)

    # pt2.toto = 3
    # print(pt2.toto)
    # print(pt2)