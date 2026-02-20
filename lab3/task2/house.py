class House:
    def __init__(self, _area=100, _price=500_000):
        self._area = _area
        self._price = _price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)

    def __str__(self):
        return f"House(area={self._area}m², price={self._price})"
