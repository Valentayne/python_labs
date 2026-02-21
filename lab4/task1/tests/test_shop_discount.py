import pytest
import allure
import sys
import os
from lab4.task1.shop import Shop

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@allure.feature("Shop")
@allure.story("Атрибути магазину")
@allure.title("Перевірка ініціалізації атрибутів Shop")
@allure.description("""
Перевіряється, що при створенні магазину
коректно встановлюються shop_name та store_type.
""")
def test_shop_attributes():
    store = Shop("TechWorld", "Electronics")
    assert store.shop_name == "TechWorld"
    assert store.store_type == "Electronics"

@allure.feature("Shop")
@allure.story("Параметри за замовчуванням")
@allure.title("Кількість товарів за замовчуванням дорівнює 0")
@allure.description("""
Якщо кількість товарів не передана,
number_of_units має бути встановлений у 0.
""")
def test_shop_default_units():
    store = Shop("TechWorld", "Electronics")
    assert store.number_of_units == 0

@allure.feature("Shop")
@allure.story("Інформація про магазин")
@allure.title("describe_shop повертає коректний опис")
@allure.description("""
Метод describe_shop повинен повертати рядок,
який містить назву магазину та тип магазину.
""")
def test_describe_shop():
    store = Shop("TechWorld", "Electronics")
    result = store.describe_shop()
    assert "TechWorld" in result
    assert "Electronics" in result

@allure.feature("Shop")
@allure.story("Стан магазину")
@allure.title("open_shop повідомляє про відкриття магазину")
@allure.description("""
Метод open_shop має повертати повідомлення
про те, що магазин відкритий.
""")
def test_open_shop():
    store = Shop("TechWorld", "Electronics")
    result = store.open_shop()
    assert "TechWorld" in result
    assert "open" in result.lower()

@allure.feature("Shop")
@allure.story("Керування кількістю товарів")
@allure.title("Встановлення кількості товарів")
@allure.description("""
Метод set_number_of_units повинен
коректно встановлювати кількість товарів.
""")
def test_set_number_of_units():
    store = Shop("TechWorld", "Electronics")
    store.set_number_of_units(100)
    assert store.number_of_units == 100

@allure.feature("Shop")
@allure.story("Керування кількістю товарів")
@allure.title("Збільшення кількості товарів")
@allure.description("""
Метод increment_number_of_units має
додавати вказану кількість товарів
до поточного значення.
""")
def test_increment_number_of_units():
    store = Shop("TechWorld", "Electronics")
    store.set_number_of_units(100)
    store.increment_number_of_units(25)
    assert store.number_of_units == 125

@allure.feature("Shop")
@allure.story("Керування кількістю товарів")
@allure.title("Збільшення кількості товарів з нуля")
@allure.description("""
Якщо кількість товарів дорівнює 0,
increment_number_of_units повинен
коректно її збільшувати.
""")
def test_increment_from_zero():
    store = Shop("TechWorld", "Electronics")
    store.increment_number_of_units(10)
    assert store.number_of_units == 10

@allure.feature("Shop")
@allure.story("Кілька екземплярів")
@allure.title("Створення кількох незалежних магазинів")
@allure.description("""
Перевіряється, що кілька екземплярів Shop
існують незалежно один від одного
та мають власні назви.
""")
def test_multiple_instances():
    s1 = Shop("Shop1", "Type1")
    s2 = Shop("Shop2", "Type2")
    s3 = Shop("Shop3", "Type3")
    assert s1.shop_name == "Shop1"
    assert s2.shop_name == "Shop2"
    assert s3.shop_name == "Shop3"

@allure.feature("Shop")
@allure.story("Керування кількістю товарів")
@allure.title("Пряма зміна кількості товарів")
@allure.description("""
Перевіряється можливість прямої зміни
поля number_of_units без використання методів.
""")
def test_change_units_directly():
    store = Shop("TestShop", "General")
    store.number_of_units = 50
    assert store.number_of_units == 50
