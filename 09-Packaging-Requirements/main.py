import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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


def info_mesurable2D(mesurable2d: Mesurable2D) -> None:
    print(mesurable2d)
    print("perimeter:", mesurable2d.perimeter())
    print("area:", mesurable2d.area())

def play_with_shapes_matching():

    c = Circle(name='C')
    poly = Polygon(name='ABCD')
    pt_a = Point(name='A')
    pt_b = Point(name='B', x=np.float64(3.0), y=np.float64(1.0))
    wp_d = WeightedPoint(name='D')
    wp_e = WeightedPoint(name='E', weight=np.float64(30.0))

    shapes: list[Shape] = [wp_d, c, poly, pt_a, pt_b, wp_e]
    points: list[Point] = []
    for s in shapes:
        match s:
            case WeightedPoint(weight=weight) if weight != 1.0:
                print("Weighted point avec poids <> 1:", s)
                points.append(s)
            case Point(x=x, y=0):
                print(f"Point sur l'axe des abscisses avec x = {x}")
                points.append(s)
            case Point(x=x, y=y):
                print(f"Point de coordonnées {x} et {y}")
                points.append(s)
            case Mesurable2D() as m:
                print(f"Mesurable 2D: aire={m.area()}, périmètre{m.perimeter()}")
            case _:
                print("SKIP:", s)

    d = pt_a.distance(pt_b)
    print("distance =", d)

    df = pd.DataFrame(
        {
            'name': [p.name for p in points],
            'x': [p.x for p in points],
            'y': [p.y for p in points],
        }
    ).sort_values(['x', 'y'])
    print(df)

    plt.plot(df.x, df.y)
    plt.show()

play_with_shapes_matching()
