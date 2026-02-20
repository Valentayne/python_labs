"""Person class."""
import datetime

class Person:
    def __init__(self, name, surname, nickname, birth_date):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.birth_date = birth_date

    @property
    def fullname(self):
        """Full name."""
        return f"{self.surname} {self.name}"

    @property
    def age(self):
        """calculate age."""
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age
