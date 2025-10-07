

from coloredpoint import ColoredPoint
from point import Point
from weightedcoloredpoint import WeightedColoredPoint
from weightedpoint import WeightedPoint


def play_with_points() -> None:
    pt1 = Point()
    pt2 = Point(name="A", x= 3.5, y=12.25)
    wpt3 = WeightedPoint()
    wpt4 = WeightedPoint(name="B", x=7.5, y=16.25, weight=5.0)
    cpt5 = ColoredPoint(color="red") 
    wcpt6 = WeightedColoredPoint(name="C", x=25.5, y=35.75, weight=255.5, color="#BD1919")

    points: list[Point] = [pt1, pt2, wpt3, wpt4, cpt5, wcpt6]
    for pt in points:
        print(pt)
        print("\t- name:", pt.name)
        print("\t- x:", pt.x)
        print("\t- y:", pt.y)
    
    _ = pt1.distance(pt2)

    # héritage sur la méthode
    _ = wpt3.distance(pt2)
    _ = cpt5.distance(pt2)
    _ = wcpt6.distance(pt2)

    # héritage sur le paramètre
    _ = pt1.distance(wpt3)
    _ = pt1.distance(cpt5)
    _ = pt1.distance(wcpt6)

    # Method Resolution Order: MRO
    print(WeightedColoredPoint.__mro__)

    print(wcpt6.__dict__)
    print(wcpt6.__class__) # builtin type()
play_with_points()