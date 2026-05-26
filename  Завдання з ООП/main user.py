from user import User
from privileges_admin import Admin

user1 = User("Олег", "Іваненко", 20, "Київ")
user2 = User("Марія", "Петренко", 22, "Львів")
user3 = User("Дмитро", "Коваль", 19, "Харків")

user1.describe_user()
user1.greeting_user()
print()

user2.describe_user()
user2.greeting_user()
print()

user3.describe_user()
user3.greeting_user()
print()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Спроби входу:", user1.login_attempts)

user1.reset_login_attempts()
print("Після скидання:", user1.login_attempts)
print()

admin = Admin("Андрій", "Бондаренко", 25, "Одеса")
admin.describe_user()
admin.priv.show_privileges()