class User():

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print("Ім'я: " + self.first_name + " " + self.last_name)
        print("Вік: " + str(self.age))
        print("Місто: " + self.city)

    def greeting_user(self):
        print("Привіт, " + self.first_name + "! Раді тебе бачити!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0