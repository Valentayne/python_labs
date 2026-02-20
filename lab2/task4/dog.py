"""class Dog"""
class Dog:
    """class Dog"""
    mammal = True
    nature = "unknown"
    breed = "unknown"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        """info"""
        return f"Name: {self.name}, Age: {self.age}"

    def voice(self):
        """voice"""
        return "Dog makes a sound"
    