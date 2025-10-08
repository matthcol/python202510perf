from model import (
    Shape,
    Point,
    WeightedPoint,
    ColoredPoint,
    WeightedColoredPoint,
    Polygon,
    Circle,
    Mesurable2D
)



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
        if isinstance(s, Mesurable2D):
            info_mesurable2D(s)
        print()
    
# TODO: match case

# PEP 636: tutorial Pattern Matching
# https://peps.python.org/pep-0636/
def play_with_shapes_matching():

    c = Circle(name='C')
    poly = Polygon(name='ABCD')
    pt_a = Point(name='A')
    pt_b = Point(name='B', x=3.0, y=1.0)
    wp_d = WeightedPoint(name='D')
    wp_e = WeightedPoint(name='E', weight=30.0)

    shapes: list[Shape] = [wp_d, c, poly, pt_a, pt_b, wp_e]
    for s in shapes:
        match s:
            case WeightedPoint(weight=weight) if weight != 1.0:
                print("Weighted point avec poids <> 1:", s)
            case Point(x=x, y=0):
                print(f"Point sur l'axe des abscisses avec x = {x}")
            case Point(x=x, y=y):
                print(f"Point de coordonnées {x} et {y}")
            case Mesurable2D() as m:
                print(f"Mesurable 2D: aire={m.area()}, périmètre{m.perimeter()}")
            case _:
                print("SKIP:", s)

def play_with_str_repr():
    pt_a = Point(name='A')
    pt = Point()
    wp_e = WeightedPoint(name='E', weight=30.0)
    cp_f = ColoredPoint(name="F", color="#0CD73F")
    wcp_h = WeightedColoredPoint(name="H", color="#B01818", weight=25.5)
    print(pt)
    print(pt_a)
    print(repr(pt_a))
    for p in pt_a, wp_e, cp_f, wcp_h:
        print(f"version str : {p}  vs version repr : {p!r}")
        p.dummy()
        print()





# play_with_points()
# play_with_mesurable2D()
# play_with_shapes_and_mesurables()
# play_with_shapes_matching()
play_with_str_repr()