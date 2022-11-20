class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

counter = Counter()
counter.increment()
counter.increment()

class DoubleCounter(Counter):


    def increment(self):
        # Counter.increment(self)
        # Counter.increment(self)
        super().increment()
        super().increment()

    def decrement(self):
        self.value -=2

    def set_zero(self):
        self.value = 0

dcounter = DoubleCounter()
# dcounter.decrement()
# print(dcounter.value)
dcounter.increment()
print(dcounter.value)

dcounter.decrement()
print(dcounter.value)

# dcounter.set_zero()
# print(dcounter.value)


class Decor:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience

    def heal(self):
        print(f"{self.name} treat")

    def ad_exp(self):
        self.experience += year

    def get_info(self):
        return f"{self.name}, {self.age}, {self.experience}, {self.salary}"



class Stom:
    def __init__(self, brunch):
        self.brunch = brunch


class Ortodent(Decor, Stom):
    def __init__(self, name, age, experience, brunch, salary):
        # super().__init__(name, age, experience)
        Decor.__init__(self, name, age, experience)
        Stom.__init__(self,brunch)
        self.salary = salary

    def get_info(self):
        all_info = super().get_info() + f"{self.brunch}  {self.salary}"
        print(all_info)

a = Ortodent("fil", 23, 4, "brecet", 10000)
a.get_info()

print(Ortodent.__mro__)



