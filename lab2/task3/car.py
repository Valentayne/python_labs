"""Car"""
class Car:
    """Car"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        """Method accelerate"""
        self.speed += 5

    def brake(self):
        """Method brake"""
        self.speed -= 5

    def get_speed(self):
        """Method get speed"""
        return self.speed