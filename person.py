class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, precent):
        self.pay = int(self.pay * (1 + precent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self,name, 'mgr', pay)

    def giveRaise(self, precent, bonus=.10):
        Person.giveRaise(self, precent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
#Manager: __init__
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)


if __name__ == '__main__':

    print('--All three--')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj.job)
        print(obj)



