from user import User

class Privileges():

    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

    def show_privileges(self):
        print("Привілеї адміністратора:")
        for p in self.privileges:
            print("- " + p)


class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.priv = Privileges()