class Car:
    def __init__(self, make, model, year, odometer=0, fuel=70):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = odometer
        self.fuel = fuel

    def __ad_distance(self, km):
        print("Before: ", self.odometr)
        self.odometr += km
        print("After: ", self.odometr)
        return self.odometr



    def __subtract_fuel(self, use_fuel):
        print("Before: ", self.fuel)
        self.fuel = self.fuel - use_fuel
        print("Afetr: ", self.fuel)
        return self.fuel



    def drive(self, km):
        if round(km / 10) > self.fuel:
            print('Need more fuel, please, fill more!')
        else:
            self.__ad_distance(km)
            self.__subtract_fuel(round(km / 10))
            print(round(km / 10))
            print('Let’s drive!')

car1 = Car('Japan', 'Nissan', 2016)
car1.drive(700)
