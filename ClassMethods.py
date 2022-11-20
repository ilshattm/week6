import  math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def frompolar(cls, radius, angle):
        """The `cls` argument is the `Point` class itself"""
        return cls(radius * math.cos(angle) , radius * math.sin(angle))

    @staticmethod
    def angle(x, y):
        """this could be outside the class, but we put it here
just because we think it is logically related to the class."""
        return math.atan2(y, x)


p1 = Point(3, 2)
p2 = Point.frompolar(3, math.pi / 4)
print(p2.x)
angle = Point.angle(3, 2)
