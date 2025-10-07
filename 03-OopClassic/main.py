from typing import List, Optional
from point import Point

print('Application Geometry')
p = Point(0.0, 0.0)
print(p)

# _ = p + (1.2, 3.4, 4.5)
# _ = p + (1.2,)
# _ = p + (1.2, 'a')
# _ = (1.2, 3.4, 4.5) + p
# _ = (1.2,) + p
# _ = (1.2, 'a') + p
# p += (1.2, 3.4, 4.5)
# p += (1.2,)
# p += (1.2, 'a')



pt: Point | None # modern declaration
# pt: Optional[Point] # old one

pt = None
pt = p

points : list[Point] = [p] # modern
# points : List[Point] = [p] # old one
