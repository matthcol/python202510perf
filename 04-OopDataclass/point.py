
from dataclasses import dataclass, field
import math

from shape import Shape


@dataclass(
    # slots=True, 
    kw_only=True, 
    # order=True,
)
class Point(Shape):
    x: float = 0.0
    y: float = 0.0

    # autre: bool = field(repr=False, default=False)
    # friends: list['Point'] = field(default_factory=list)

    # # equivalent généré
    # def __init__(self, x: float = 0.0, y: float = 0.0, autre: bool = False, friends: list['Point'] | None = None):
    #     self.friends: list['Point']
    #     if friends is None:
    #         self.friends = []
    #     else:
    #         self.friends = friends 

    def distance(self, other: 'Point') -> float:
        return math.dist((self.x, self.y), (other.x, other.y))

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