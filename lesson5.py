class Point:

    def __init__(self,x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"object x = {self.x}, y = {self.y}"

    def __add__(self, other):
        if isinstance(other, Point):
            result = self.x * self.y + other.x * other.y
            return result
        elif (f"{other} является обьектом Point!!!")
        raise Exception(f"{other} является обьектом Point!!!")

    def __radd__(self, other):
        if isinstance(other, Point):
            raise Exception(f"{other} является обьектом Point!!!")
        result = self.x * self.y + other
        return result
__sub__
__div__

obj = Point(6, 3)
obj1 = Point(9, 3)
print(8 + obj1)
# print(obj + obj1)