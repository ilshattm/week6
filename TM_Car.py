class Car:
    def __init__(self, make, model, year, odometer=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel

    def __add_distance(self, km):
        self.odometer += km
        return self.odometer


    def __subtract_fuel(self, km):
        self.fuel = self.fuel - round(km / 10)
        return self.fuel



    def drive(self, km):
        if round(km / 10) > self.fuel or km < 0:
            print('Need more fuel, please, fill more!')
        else:
            self.__add_distance(km)
            print(self.odometer)
            self.__subtract_fuel(km)
            print(self.fuel)
            print('Let’s drive!')

car1 = Car('Japan', 'Nissan', 2016)
car1.drive(-30)

class Car:
    def __init__(self, make, model, year, odometer=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel
    def __ad_distance(self, dist):
        self.odometer += dist
        return self.odometer
    def __subtract_fuel(self, dist):
        use_fuel = round(dist / 10)
        self.fuel = self.fuel - use_fuel
        return self.fuel
    def drive(self, dist):
        use_fuel = round(dist / 10)
        if use_fuel <= self.fuel or dist < 0:
            self.__ad_distance(dist)
            self.__subtract_fuel(dist)
            print("Let’s drive!")
        else:
            print("Need more fuel, please, fill more!")