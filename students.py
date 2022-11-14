from random import randint
class Students:
    def __init__(self, full_name, course):
        self.full_name = full_name
        self.course = course
        self.subject = {}
        self.total = 0

    def set_subject(self, subjects: dict) -> None:
        self.subjects = subjects

    def get_total(self):
        self.total = sum(self.subjects.values()) / len(self.subjects)

    def save_total_in_file(self):
        with open(f"{self.full_name}.txt", "a") as f:
            f.write(f"{self.full_name} - {self.course} - {self.total}\n")
            for key, value in self.subjects.items():
                f.write(f"{key} - {value}\n ")
        self.total = 0
        self.subjects = {}


    def set_course(self):
        self.course += 1



subjects1 = {
            "Architecture": randint(1, 100),
            "Art & Design": randint(1, 100),
            "Accounting & Finance": randint(1, 100),
            "Computer Science & Information Systems": randint(1, 100),
            "Engineering & Technology": randint(1, 100)
     }
subjects2 = {
            "Medicine": randint(1, 100),
            "Economics & Econometrics": randint(1, 100),
            "Law": randint(1, 100)

     }




nazgul = Students("Tab Naz", 3)
nazgul.set_subject(subjects1)
nazgul.get_total()
nazgul.save_total_in_file()
nazgul.set_course()
nazgul.set_subject(subjects2)
nazgul.get_total()
nazgul.save_total_in_file()