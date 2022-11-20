

#
# class Product:
#     def __init__(self, name:str, price:int):
#         self.name = name
#         self.price = price
#
#
#     def get_info(self):
#         print(f"{self.name} - {self.price}")
#
#
# potato = Product("potato", 25)
# potato.get_info()
import uuid

class Bank:
    def __init__(self, name: str):
        self.name = name
        self.__generate_account()


    def __generate_account(self):
        self.__account = str(uuid.uuid4())

    @property
    def account(self):
        # self.__generate_account()
        print(f"Your account {self.__account}")


    @account.setter
    def account(self, key:str):
        self.__account =  str(uuid.uuid4()) + key


nazgul = Bank("Nazgul")
nazgul.account
nazgul.account = " no_name"
nazgul.account