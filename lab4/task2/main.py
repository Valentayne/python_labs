from lab4.task2.user import User
from lab4.task2.admin import Admin

user1 = User("Alice", "Smith", "alice@example.com", "alice_s", newsletter=True)
user2 = User("Bob", "Jones", "bob@example.com", "bobby")
user3 = User("Carol", "White", "carol@example.com", "carol_w", newsletter=True)

for u in [user1, user2, user3]:
    print(u.describe_user())
    print(u.greeting_user())

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
print(admin.describe_user())
print(admin.show_privileges())