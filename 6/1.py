class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


user_account = UserAccount('John Doe', 'anonimamomin@gmail.com', 'qwerty123')
user_account.set_password('ivanzolo2004')
print(user_account.check_password('ivanzolo2004'))





