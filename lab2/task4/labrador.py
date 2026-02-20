from lab2.task4.dog import Dog


class Labrador(Dog):
    nature = "friendly"
    breed = "Labrador"

    def voice(self):
        return "Labrador says: Woof!"