list = ["sdfdfd", "sdfdsfd", "Fort"]

class Registration:
    def __init__(self, username:str, password:str, email:str):
        self.username = self.__validate_username(username)
        self.password = self.__valid_password(password)
        self.email = email

    def get_info(self):
        print(f"username: {self.username} - password: {self.password} - email: {self.email}")

    #
    # def validate_username(self, username):
    #     if username in list:
    #         print("Error Username has been creat")
    #     else:
    #         list.append(username)
    #         self.username = username


    def __validate_username(self,username):
        if username not in list:
            list.append(username)
            return username
        else:
            raise Exception("username not unic")

    def __valid_password(self, password):
        if len(password) < 8 or password.isalpha() or password.isdigit() or password[0].islower():
            raise Exception("Пароль должен содержать не менее 8 символов включая символы и числа")
        return password

log1 = Registration("Forte", "H889fejууi", "iii@gmail.com")
log1.get_info()
