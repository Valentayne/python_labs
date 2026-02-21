import pytest
import sys
import os
import allure
from lab4.task2.user import User
from lab4.task2.admin import Admin
from lab4.task2.privileges import Privileges

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@allure.feature("User")
@allure.story("Атрибути користувача")
@allure.title("Перевірка ініціалізації атрибутів користувача")
@allure.description("""
Перевіряється, що всі передані атрибути користувача
(first_name, last_name, email, nickname, newsletter)
коректно зберігаються під час створення об'єкта User.
""")
def test_user_attributes():
    u = User("Alice", "Smith", "alice@example.com", "alice_s", newsletter=True)
    assert u.first_name == "Alice"
    assert u.last_name == "Smith"
    assert u.email == "alice@example.com"
    assert u.nickname == "alice_s"
    assert u.newsletter is True

@allure.feature("User")
@allure.story("Параметри за замовчуванням")
@allure.title("Newsletter за замовчуванням вимкнений")
@allure.description("""
Якщо параметр newsletter не передано,
він має бути встановлений у False.
""")
def test_user_default_newsletter():
    u = User("Bob", "Jones", "bob@example.com", "bobby")
    assert u.newsletter is False

@allure.feature("User")
@allure.story("Безпека")
@allure.title("Login attempts за замовчуванням дорівнює 0")
@allure.description("""
Перевіряється, що кількість спроб входу
при створенні користувача дорівнює нулю.
""")
def test_user_default_login_attempts():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    assert u.login_attempts == 0

@allure.feature("User")
@allure.story("Інформація про користувача")
@allure.title("describe_user повертає коректний опис")
@allure.description("""
Метод describe_user повинен повертати рядок,
який містить ім'я, прізвище, email та nickname користувача.
""")
def test_describe_user():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    result = u.describe_user()
    assert "Alice" in result
    assert "Smith" in result
    assert "alice@example.com" in result
    assert "alice_s" in result

@allure.feature("User")
@allure.story("Вітання")
@allure.title("greeting_user містить nickname користувача")
@allure.description("""
Перевіряється, що метод greeting_user
повертає привітання з nickname користувача.
""")
def test_greeting_user():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    result = u.greeting_user()
    assert "alice_s" in result

@allure.feature("User")
@allure.story("Безпека")
@allure.title("Збільшення кількості спроб входу")
@allure.description("""
Метод increment_login_attempts має
коректно збільшувати лічильник login_attempts.
""")
def test_increment_login_attempts():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    u.increment_login_attempts()
    u.increment_login_attempts()
    u.increment_login_attempts()
    assert u.login_attempts == 3

@allure.feature("User")
@allure.story("Безпека")
@allure.title("Скидання спроб входу")
@allure.description("""
Метод reset_login_attempts повинен
скидати login_attempts до 0.
""")
def test_reset_login_attempts():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    u.increment_login_attempts()
    u.increment_login_attempts()
    u.reset_login_attempts()
    assert u.login_attempts == 0

@allure.feature("Privileges")
@allure.story("Параметри за замовчуванням")
@allure.title("Порожній список привілеїв за замовчуванням")
@allure.description("""
Якщо привілеї не передані,
список privileges має бути порожнім.
""")
def test_privileges_default():
    p = Privileges()
    assert p.privileges == []

@allure.feature("Privileges")
@allure.story("Відображення привілеїв")
@allure.title("show_privileges повертає список привілеїв")
@allure.description("""
Метод show_privileges повинен повертати
список привілеїв без змін.
""")
def test_privileges_show():
    items = ["Allowed to add message", "Allowed to delete users"]
    p = Privileges(items)
    assert p.show_privileges() == items

@allure.feature("Admin")
@allure.story("Наслідування")
@allure.title("Admin наслідує клас User")
@allure.description("""
Перевіряється, що об'єкт Admin
є екземпляром класу User.
""")
def test_admin_inherits_user():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    assert isinstance(admin, User)

@allure.feature("Admin")
@allure.story("Привілеї адміністратора")
@allure.title("Admin має об'єкт Privileges")
@allure.description("""
Клас Admin повинен містити атрибут priv,
який є екземпляром класу Privileges.
""")
def test_admin_has_priv():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    assert isinstance(admin.priv, Privileges)

@allure.feature("Admin")
@allure.story("Привілеї адміністратора")
@allure.title("Admin має стандартні привілеї")
@allure.description("""
Якщо привілеї не передані явно,
Admin повинен мати стандартний набір привілеїв.
""")
def test_admin_default_privileges():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    privs = admin.show_privileges()
    assert len(privs) > 0

@allure.feature("Admin")
@allure.story("Привілеї адміністратора")
@allure.title("Admin підтримує кастомні привілеї")
@allure.description("""
Перевіряється, що Admin може приймати
та повертати користувацький список привілеїв.
""")
def test_admin_custom_privileges():
    custom = ["Allowed to add message", "Allowed to ban users"]
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin", privileges=custom)
    assert admin.show_privileges() == custom

@allure.feature("Admin")
@allure.story("Інформація про адміністратора")
@allure.title("Admin.describe_user працює коректно")
@allure.description("""
Метод describe_user адміністратора
повинен містити ім'я та прізвище.
""")
def test_admin_describe_user():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    result = admin.describe_user()
    assert "Dan" in result
    assert "Admin" in result

@allure.feature("Admin")
@allure.story("Вітання")
@allure.title("Admin.greeting_user містить nickname")
@allure.description("""
Метод greeting_user для Admin
повинен повертати привітання з nickname.
""")
def test_admin_greeting():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    result = admin.greeting_user()
    assert "dan_admin" in result

@allure.feature("Admin")
@allure.story("Безпека")
@allure.title("Admin: збільшення та скидання login attempts")
@allure.description("""
Перевіряється робота increment_login_attempts
та reset_login_attempts для адміністратора.
""")
def test_admin_login_attempts():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    admin.increment_login_attempts()
    admin.increment_login_attempts()
    assert admin.login_attempts == 2
    admin.reset_login_attempts()
    assert admin.login_attempts == 0