from lab3.task2.house import House


class SmallHouse(House):
    def __init__(self, _price=200_000):
        super().__init__(_area=40, _price=_price)
