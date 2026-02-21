import pytest
import sys
import os
from lab4.task2.user import User
from lab4.task2.admin import Admin
from lab4.task2.privileges import Privileges

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_user_attributes():
    u = User("Alice", "Smith", "alice@example.com", "alice_s", newsletter=True)
    assert u.first_name == "Alice"
    assert u.last_name == "Smith"
    assert u.email == "alice@example.com"
    assert u.nickname == "alice_s"
    assert u.newsletter is True


def test_user_default_newsletter():
    u = User("Bob", "Jones", "bob@example.com", "bobby")
    assert u.newsletter is False


def test_user_default_login_attempts():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    assert u.login_attempts == 0


def test_describe_user():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    result = u.describe_user()
    assert "Alice" in result
    assert "Smith" in result
    assert "alice@example.com" in result
    assert "alice_s" in result


def test_greeting_user():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    result = u.greeting_user()
    assert "alice_s" in result


def test_increment_login_attempts():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    u.increment_login_attempts()
    u.increment_login_attempts()
    u.increment_login_attempts()
    assert u.login_attempts == 3


def test_reset_login_attempts():
    u = User("Alice", "Smith", "alice@example.com", "alice_s")
    u.increment_login_attempts()
    u.increment_login_attempts()
    u.reset_login_attempts()
    assert u.login_attempts == 0


def test_privileges_default():
    p = Privileges()
    assert p.privileges == []


def test_privileges_show():
    items = ["Allowed to add message", "Allowed to delete users"]
    p = Privileges(items)
    assert p.show_privileges() == items


def test_admin_inherits_user():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    assert isinstance(admin, User)


def test_admin_has_priv():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    assert isinstance(admin.priv, Privileges)


def test_admin_default_privileges():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    privs = admin.show_privileges()
    assert len(privs) > 0


def test_admin_custom_privileges():
    custom = ["Allowed to add message", "Allowed to ban users"]
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin", privileges=custom)
    assert admin.show_privileges() == custom


def test_admin_describe_user():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    result = admin.describe_user()
    assert "Dan" in result
    assert "Admin" in result


def test_admin_greeting():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    result = admin.greeting_user()
    assert "dan_admin" in result


def test_admin_login_attempts():
    admin = Admin("Dan", "Admin", "dan@example.com", "dan_admin")
    admin.increment_login_attempts()
    admin.increment_login_attempts()
    assert admin.login_attempts == 2
    admin.reset_login_attempts()
    assert admin.login_attempts == 0