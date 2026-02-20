"""Main"""
from lab2.task1.bank import Bank
from lab2.task3.car import Car
from lab2.task2.coin import Coin
from lab2.task4.buldog import Bulldog
from lab2.task4.labrador import Labrador
from lab2.task4.pets import Pets
from lab2.task4.poodle import Poodle
from lab2.task5.buffer import Buffer
from lab2.task6.name_length_error import NameLengthError
from lab2.task7.decimal_to_roman import DecimalToRoman
from lab2.task7.roman_to_decimal import RomanToDecimal
from lab2.task8.discount import Discount
from lab2.task8.shop import Shop
from lab2.task9.admin import Admin
from lab2.task9.user import User


def bank():
    """Bank"""
    money = int(input("Enter account money: "))
    account = Bank(money)
    print("""
    Existing commands
    deposit
    withdraw
    balance
    Write exit to quit
    """)
    while True:
        command = input("Enter command: ")
        if command == "deposit":
            summa = int(input("Enter summa: "))
            account.deposit(summa)
        if command == "withdraw":
            summa = int(input("Enter summa: "))
            print(account.withdraw(summa))
        if command == "balance":
            print(account.checkout())
        if command == "exit":
            break

def coin():
    """Coin"""
    n = int(input("Enter quantity of toss: "))

    coin = Coin()

    for i in range(1, n + 1):
        result = coin.toss()
        print(f"Toss {i}: {result}")

def car():
    """Car"""
    data = list(input("Enter car brand model and year trough a space: ").strip().split())
    car = Car(data[0], data[1], data[2])

    print("Прискорення:")
    for _ in range(5):
        car.accelerate()
        print(car.get_speed())

    print("\nГальмування:")
    for _ in range(5):
        car.brake()
        print(car.get_speed())

def pets():
    """Pets"""
    dog1 = Labrador("Buddy", 3)
    dog2 = Poodle("Luna", 5)
    dog3 = Bulldog("Rocky", 2)

    my_pets = Pets()
    my_pets.add_pet(dog1)
    my_pets.add_pet(dog2)
    my_pets.add_pet(dog3)

    my_pets.show_pets()

    print(dog1.voice())
    print(dog2.trick())
    print(dog3.guard())

def buffer():
    """Buffer"""
    buf = Buffer()

    buf.add(1, 2, 3)
    print(buf.get_current_part())

    buf.add(4, 5, 6, 7, 8, 9)
    print(buf.get_current_part())

    buf.add(10, 11)
    print(buf.get_current_part())

def check_name(name):
    if len(name) < 10:
        raise NameLengthError(name)

def length_name():
    try:
        check_name("Alex")
    except NameLengthError as e:
        print(e)

    check_name("AlexanderTheGreat")

def decimal_to_roman():
    converter = DecimalToRoman()
    print(converter.convert(1987))

def roman_to_number():
    converter = RomanToDecimal()
    print(converter.convert("MCMLXXXVII"))

def shop():
    store = Shop("TechStore", "Electronics")

    print(store.shop_name)
    print(store.store_type)

    store.describe_shop()
    store.open_shop()

    print(store.number_of_units)
    store.number_of_units = 25
    print(store.number_of_units)

    store.set_number_of_units(40)
    print(store.number_of_units)

    store.increment_number_of_units(10)
    print(store.number_of_units)

    store1 = Shop("BookWorld", "Books")
    store2 = Shop("FashionHub", "Clothes")
    store3 = Shop("GameZone", "Games")

    store1.describe_shop()
    store2.describe_shop()
    store3.describe_shop()

    store_discount = Discount(
        "SaleStore",
        "Mixed",
        ["Laptop", "Headphones", "Keyboard"]
    )

    store_discount.get_discount_products()

def user_operations():
    user1 = User("Ivan", "Petrenko", "ivan@gmail.com", "ivan_pet", True)
    user2 = User("Olena", "Shevchenko", "olena@gmail.com", "olena_s", False)

    user1.describe_user()
    user1.greeting_user()

    user2.describe_user()
    user2.greeting_user()

    user1.increment_login_attempts()
    user1.increment_login_attempts()
    user1.increment_login_attempts()

    print(user1.login_attempts)

    user1.reset_login_attempts()
    print(user1.login_attempts)

def work_with_admin():
    admin = Admin(
        "Admin",
        "Root",
        "admin@gmail.com",
        "root_admin",
        True,
    )

    admin.describe_user()
    admin.priv.show_privileges()

def run_script():
    """Run script"""
    while True:
        task = int(input("Please enter your task from 1 to 9: "))
        match task:
            case 1:
                bank()
            case 2:
                 coin()
            case 3:
                car()
            case 4:
                pets()
            case 5:
                buffer()
            case 6:
                length_name()
            case 7:
                decimal_to_roman()
                roman_to_number()
            case 8:
                shop()
            case 9:
                user_operations()
                work_with_admin()

if __name__ == '__main__':
    run_script()
