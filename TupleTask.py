class ChangTuple(tuple):
    pass

    def append(self, added):
        ltuple =list(self)
        ltuple.append(added)
        print(ltuple)
        ltuple = tuple(ltuple)
        print(ltuple)

        return ltuple
b = ChangTuple("Artefact")
a = tuple("hgdj")
print(b)
p = b.append([9,0])
print(p)



class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display(self):
        all_info = f"name - {self.name}  age - {self.age}  "
        return all_info
class Student(Person):

    def __init__(self, name, age, department: str):
        super().__init__(name, age)
        self.department = department

    def displayStudent(self):
        allinfo = super().display() + f"department - {self.department}"
        print(allinfo)

student1 = Student("Fadeev", 23, "pedagogia")
student1.displayStudent()


class Abonent:
    def __init__(self, id_number:int, full_name:str, address:str, credite:int, card_number:int, debet:int, call_time:int):
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
    def get_overused(cls, abos:list):
        new_abon = []
        for item in abos:
            if item.call_time > 15:
                    new_abon.append(f"FullName - {item.full_name},  AbonentID - {item.id_number}")
                    print(f" FullName - {item.full_name}  CardNumber - {item.card_number}  Number - {item.id_number}")
        return new_abon

    @classmethod
    def sort_abo(cls, abos:list):
        new_abon = []
        for item in abos:
                new_abon.append(item.full_name)
        new_abon.sort()
        return new_abon

Abon1 = Abonent(1001, "Dvanov Ivan Ivanovich", "Moscow, 1 street, apt. 1", 500, 1234_1222_2312_0001, 1000, 30)
Abon2 = Abonent(1002, "Ivanov IvEn Ivanovich", "NY, 26 street, apt. 1", 600, 1234_1222_2312_0002, 1000, 12)
Abon3 = Abonent(1003, "Saburov IvEn Ivanovich", "Bost, 34 street, apt. 1", 300, 1234_1222_2312_0003, 10000, 2)
Abon4 = Abonent(1004, "Adoans Evgen Ivanovich", "NY, 26 street, apt. 1", 200, 1234_1222_2312_0002, 5000, 116)

list1 = [Abon1, Abon2, Abon3, Abon4]
# Abon1.display_info()


l1 = Abonent.get_overused(list1)
l2 = Abonent.sort_abo(list1)

print(l1)
print(l2)


class Person:

    def __init__(self, full_name:str, address:str, age=18):
        self.full_name = full_name
        self.age = age
        self.address = address


    def talk(self):
        print(f"Такой-то  {self.full_name} говорит")


    def move(self, new_address:str):
        self.address = new_address


    def __str__(self):
        return f'{self.full_name} {self.age} {self.address}'




p1 = Person("juk", "Msc, 12 av, apt 3")
p1.__str__()
print(p1)

p1.talk()

p1.move("Bishkek, Chuy, 12-23")
p1.__str__()
print(p1)

# class Abonent:
#     def __init__(self, id_number:int, full_name:str, address:str, credite:int, card_number:int, debet:int, call_time_city:int, call_time_intercity: int):
#         self.id_number = id_number
#         self.full_name = full_name
#         self.address = address
#         self.credite = credite
#         self.card_number = card_number
#         self.debet = debet
#         self.call_time_city = call_time_city
#         self.call_time_intercity = call_time_intercity
#
#     def display_info(self):
#         print(f" ФИО {self.full_name},  номер кредитной карты - {self.card_number},  номер - {self.id_number}")
#
#     @classmethod
#     def get_overused(cls, abos:list):
#         new_abon = []
#         for item in abos:
#             if item.call_time_intercity > 15:
#                     new_abon.append(f"FullName - {item.full_name},  AbonentID - {item.id_number}")
#                     print(f" FullName - {item.full_name}  CardNumber - {item.card_number}  Number - {item.id_number}")
#         return new_abon
#
#     @classmethod
#     def sort_abo(cls, abos:list):
#         new_abon = []
#         new_dict = {}
#         for item in abos:
#                 new_abon.append(item.full_name)
#                 new_dict.update({f"{item.full_name}": f"{item}"})
#         new_abon.sort()
#         print(new_abon)
#         print(new_dict)
#         new_list = []
#         for item in new_abon:
#             new_list.append(new_dict[item])
#         print(new_list)
#         return new_list
#         # return new_abon
#         # for item in new_abon:
#         #     if item == abos.:
#         #         print(f"{cls}")
# Abon1 = Abonent(1001, "Dvanov Ivan Ivanovich", "Moscow, 1 street, apt. 1", 500, 1234_1222_2312_0001, 1000, 30, 16)
# Abon2 = Abonent(1002, "Ivanov IvEn Ivanovich", "NY, 26 street, apt. 1", 600, 1234_1222_2312_0002, 1000, 12, 84)
# Abon3 = Abonent(1003, "Saburov IvEn Ivanovich", "Bost, 34 street, apt. 1", 300, 1234_1222_2312_0003, 10000, 2, 2)
# Abon4 = Abonent(1004, "Adoans Evgen Ivanovich", "NY, 26 street, apt. 1", 200, 1234_1222_2312_0002, 5000, 116, 43)
#
# list1 = [Abon1, Abon2, Abon3, Abon4]
#
# l1 = Abonent.get_overused(list1)
# l2 = Abonent.sort_abo(list1)

# print(l1)
# print(l2)


class Abonent:
    def __init__(self, id_number: int, full_name: str, address: str, credite: int, card_number: int, debet: int,
                 call_time: int):
        self.id_number = id_number
        self.full_name = full_name
        self.address = address
        self.credite = credite
        self.card_number = card_number
        self.debet = debet
        self.call_time = call_time

    def display_info(self):
        print(f" ФИО {self.full_name},  номер кредитной карты - {self.card_number},  номер - {self.id_number}")

    @classmethod
    def get_overused(cls, abos: list):
        new_abon = []
        for item in abos:
            if item.call_time > 15:
                new_abon.append(item)

        return new_abon

    @classmethod
    def sort_abo(cls, abos: list):
        new_abon = []
        new_dict = {}
        for item in abos:
            new_abon.append(item.full_name)
            new_dict.update({f"{item.full_name}": item})
        new_abon.sort()
        print(new_abon)
        print(new_dict)

        new_list = []
        for item in new_abon:
            new_list.append(new_dict[item])
        return new_list


Abon1 = Abonent(1001, "Dvanov Ivan Ivanovich", "Moscow, 1 street, apt. 1", 500, 1234_1222_2312_0001, 1000, 30)
Abon2 = Abonent(1002, "Ivanov IvEn Ivanovich", "NY, 26 street, apt. 1", 600, 1234_1222_2312_0002, 1000, 12)
Abon3 = Abonent(1003, "Saburov IvEn Ivanovich", "Bost, 34 street, apt. 1", 300, 1234_1222_2312_0003, 10000, 2)
Abon4 = Abonent(1004, "Adoans Evgen Ivanovich", "NY, 26 street, apt. 1", 200, 1234_1222_2312_0002, 5000, 116)

list1 = [Abon1, Abon2, Abon3, Abon4]

l1 = Abonent.get_overused(list1)
l2 = Abonent.sort_abo(list1)

print(l1)
print(l2)


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
        return f"{self.full_name}, {self.card_number}, {self.id_number}"
    @classmethod
    def sort_abo(cls, abos):
        abos.sort(key=lambda x: x.full_name)
        return abos

    @classmethod
    def get_overused(cls, abos):
        overused_abos = [x for x in abos if x.call_time > 15]
        return overused_abos