

from circle import Circle
from coloredpoint import ColoredPoint
from mesurable import Mesurable2D
from point import Point
from polygon import Polygon
from shape import Shape
from weightedcoloredpoint import WeightedColoredPoint
from weightedpoint import WeightedPoint


def play_with_points() -> None:
    # s = Shape() 
    pt1 = Point()
    pt2 = Point(name="A", x= 3.5, y=12.25)
    wpt3 = WeightedPoint()
    wpt4 = WeightedPoint(name="B", x=7.5, y=16.25, weight=5.0)
    cpt5 = ColoredPoint(color="red") 
    wcpt6 = WeightedColoredPoint(name="C", x=25.5, y=35.75, weight=255.5, color="#BD1919")
    pt7 = Point.from_coords(1.0, 2.0)
    wpt8 = WeightedPoint.from_coords(3.0, 4.0)

    points: list[Point] = [pt1, pt2, wpt3, wpt4, cpt5, wcpt6, pt7, wpt8]
    for pt in points:
        print(pt)
        print("\t- name:", pt.name)
        print("\t- x:", pt.x)
        print("\t- y:", pt.y)
        pt.translate(1.0, -1.0)
    
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


def info_mesurable2D(mesurable2d: Mesurable2D) -> None:
    print(mesurable2d)
    print("perimeter:", mesurable2d.perimeter())
    print("area:", mesurable2d.area())

def play_with_mesurable2D() -> None:
    c = Circle()
    poly = Polygon()
    pt = Point()
    # info_mesurable2D(pt)
    
    for m in c, poly:
        info_mesurable2D(m)

def play_with_shapes_and_mesurables() -> None:
    c = Circle(name='C')
    poly = Polygon(name='ABCD')
    pt = Point(name='A')

    shapes: list[Shape] = [c, poly, pt]
    
    for s in shapes:
        print(s.name)
        if isinstance(s, Mesurable2D): # nécessite @runtime_checkable
            info_mesurable2D(s)
        print()

def play_with_shapes_and_mesurables2() -> None:
    c = Circle(name='C')
    poly = Polygon(name='ABCD')
    pt = Point(name='A')

    shapes: list[Shape] = [c, poly, pt]
    
    for s in shapes:
        print(s.name)
        # verification dynamique (idée)
        if hasattr(s, 'perimeter') and hasattr(s, 'area'): 
            info_mesurable2D(s) # type: ignore
        print()
    
# TODO: match case

# play_with_points()

# play_with_mesurable2D()

play_with_shapes_and_mesurables2()