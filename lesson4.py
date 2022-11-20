# mro


# staticmethod, classmethod, instance method

from datetime import datetime


#
# class B:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Person:
#     spec = "Progammist"
#     it_major = ["pm", "devops", "tester", "developer", "analytyc", "ux-ui"]
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def create_object(cls, name, year):
#         now_date = datetime.now().year
#         age = now_date - year
#         return cls(name, age)
#
#     @classmethod
#     def get_object_with_cls(cls, list_object_person):
#         for i in list_object_person:
#             if isinstance(i, cls):
#                 print(i.name)
#                 print(i.age)
#
#     def get_person(self):
#         print("{name} {age}".format(name=self.name, age=self.age))
#
#
# a = B("Aliza", 16)
# sman = Person("Sman", 23)
# aidana = Person("Aidana", 22)
# nazgul = Person.create_object("Nazgul", 1998)
#
# nazgul.get_person()

# lists = [sman, aidana, a]
# Person.create_object_with_cls(lists)


class Student:

    def __init__(self, name: str, group: str, age: int, course: int):
        self.name = name
        self.group = group
        self.age = age
        self.course = course

    @classmethod
    def create_object(cls, dicta:dict):
        now_date = datetime.now().year
        age = now_date - dicta["year"]
        course = now_date - dicta["year_add_vuz"]
        return cls(dicta["name"], dicta["group"], age, course)

    def get_person(self):
        print(
            "{name} {group} {age} {course}".format(name=self.name, group=self.group, age=self.age, course=self.course))


    @staticmethod
    def det_vuz_add_year(course):
        now_date = datetime.now().year
        print(now_date - course)
        return now_date - course

dict = {
    "name": "George",
    "group": "IT",
    "year": 2003,
    "year_add_vuz": 2019
}

stud1 = Student.create_object(dict)
stud1.get_person()

stud1.det_vuz_add_year(3)