from typing import List, Optional
from point import Point

print('Application Geometry')
p = Point(0.0, 0.0)
print(p)


pt: Point | None # modern declaration
# pt: Optional[Point] # old one

pt = None
pt = p

points : list[Point] = [p] # modern
# points : List[Point] = [p] # old one
