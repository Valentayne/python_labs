"""Main module."""

import os
import datetime
from person import Person


def modifier(filename):
    """ modify data """
    persons = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines[1:]:
        name, surname, nickname, birth_date_str = line.strip().split(";")
        birth_date = datetime.datetime.strptime(
            birth_date_str, "%Y-%m-%d"
        ).date()

        persons.append(Person(name, surname, nickname, birth_date))

    dir_name = os.path.dirname(filename)
    base_name = os.path.basename(filename)

    new_filename = os.path.join(dir_name, "modified_" + base_name)

    with open(new_filename, "w", encoding="utf-8") as file:
        file.write("name;fullname;surname;nickname;birth_date;age\n")

        for p in persons:
            file.write(
                f"{p.name};{p.fullname};{p.surname};"
                f"{p.nickname};{p.birth_date};{p.age}\n"
            )

    print(f"Файл створено: {new_filename}")

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "people.txt")

    modifier(file_path)