class Phone:
    def __init__(self, number: int, model: str, weight: int):
        self.number = number
        self.model = model
        self.weight = weight

    def get_info(self):
        print(f"Number - {self.number}  Model - {self.model} Weight - {self.weight}")

    def sendMessage(self, number_of_phon):
        for i in number_of_phon:
            print(f"Pushed massage to number {i.number}")


phone1 = Phone(990000001, "Samsung", 120)
phone2 = Phone(990000002, "Ericson", 220)
phone3 = Phone(990000003, "Nokia", 320)

phone1.get_info()
phone2.get_info()
phone3.get_info()

list1 = [phone1, phone2, phone3]
phone1.sendMessage(list1)

