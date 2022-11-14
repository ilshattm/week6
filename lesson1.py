#polimorfizm
from random import randint
class Triangle:
    def __init__(self, count= 3) -> None:
        self.names_values = {f'side_{i}': randint(1, 200) for i in range(count)}
        self.square = 0

    def get_attrs(self) -> dict:
        print(self.__dict__)

    def distract_square(self) -> None:
        square = 1 / 2 * self.names_values["side_0"] * self.names_values["side_1"]
        self.square = square
        print(self.square)

    def get_list_attrs(self):
        lists = list(self.__dict__.items())
        print(lists)

class Regtanglr:
    def __init__(self, a, b)  -> None:
        self.side_a = a
        self.side_b = b
        self.square = 0


    def get_attrs(self) -> dict:
        print(self.__dict__)

    def distract_square(self) -> None:
        self.square = self.side_a * self.side_b
        print(self.square)

    def get_list_attrs(self):
        lists = list(self.__dict__.items())
        print(lists)



triangle1 = Triangle()
triangle2 = Triangle()
regtriangle1 = Regtanglr(12, 4)
regtriangle2 = Regtanglr(32, 3)

lists = (triangle1, regtriangle1, regtriangle2, triangle2)

for i in lists:
    i.distract_square()
    i.get_attrs()
    i.get_list_attrs()


