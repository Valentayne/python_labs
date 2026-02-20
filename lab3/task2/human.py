class Human:
    default_name = 'John Doe'
    default_age = 30

    def __init__(self, name, age, money, house=None):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, "
              f"Гроші: {self.__money}, Будинок: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Стандартне ім'я: {Human.default_name}, Стандартний вік: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self, amount):
        self.__money += amount
        print(f"Поповнення рахунку на {amount}. Поточний баланс: {self.__money}")

    def buy_house(self, house, discount=10):
        price = house.final_price(discount)
        if self.__money < price:
            print(f"Недостатньо грошей! Потрібно {price:.2f}, є {self.__money}")
        else:
            self.__make_deal(house, price)
            print(f"Будинок куплено за {price:.2f}!")

