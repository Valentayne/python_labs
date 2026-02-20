from lab3.task2.human import Human
from lab3.task2.small_house import SmallHouse

if __name__ == '__main__':
    print("=== Довідковий метод ===")
    Human.default_info()

    print("\n=== Створення об'єкта людини ===")
    person = Human(name='Олег', age=35, money=50_000)
    person.info()

    print("\n=== Створення SmallHouse ===")
    small = SmallHouse(_price=300_000)
    print(small)

    print("\n=== Спроба купити будинок (недостатньо грошей) ===")
    person.buy_house(small)

    print("\n=== Поповнення рахунку ===")
    person.earn_money(350_000)

    print("\n=== Повторна спроба купити будинок ===")
    person.buy_house(small)

    print("\n=== Стан після покупки ===")
    person.info()