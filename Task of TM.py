# пишите код внизу
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"



class Bus(Vehicle):
    def __init__(self, name, max_speed:int, mileage:int):
        Vehicle.__init__(self, name, max_speed, mileage)
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


bus1 = Bus("Sb", 60, 1000)
print(bus1.name)
print(bus1.seating_capacity())



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return self.width * 2 + self.length * 2

    def square(self):
        return self.length * self.width

    def change_params(self, length, width):
        self.length = length
        self.width = width


    def print_params(self):
        print(f" Length - {self.length}  Width -  {self.width}")


rec1 = Rectangle(5, 7)
rec1.print_params()
print(rec1.perimeter())
print(rec1.square())
rec1.change_params(2, 5)
rec1.print_params()
print(rec1.perimeter())


class ContactList(list):
    def search_by_name(self, name):
        return [names for names in self if name == names]

list1 = ContactList("dodo")
print(list1.search_by_name("y"))


class Airplane:
    def __init__(self, make: str, model: str, year: int, max_speed: int, odometer=0, is_flying=False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying

    def take_off(self):
        self.is_flying = True
        return self.is_flying

    def land(self):
        self.is_flying = False
        return self.is_flying

    def fly(self, distance):
        self.odometer += distance
        return self.odometer

airplane1 = Airplane("US", "Abs1298", 2015, 500)
airplane1.take_off()
airplane1.land()
airplane1.fly(2000)


class Abonent:
    def __init__(self, id_number, full_name, address, credite, card_number, debet, call_time):
        self.id_number = id_number
        self.full_name = full_name
        self.address = address
        self.credite = credite
        self.card_number = card_number
        self.debet = debet
        self.call_time = call_time

    def display_info(self):
        print(f" FullName - {self.full_name}  CardNumber - {self.card_number}  Number - {self.id_number}")

    @classmethod
    def get_overused(cls, abos):
        if cls.call
