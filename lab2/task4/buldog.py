from lab2.task4.dog import Dog


class Bulldog(Dog):
    nature = "calm"
    breed = "Bulldog"

    def guard(self):
        return "Bulldog is guarding the house"