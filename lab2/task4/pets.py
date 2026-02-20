class Pets:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def show_pets(self):
        for pet in self.pets:
            print(
                f"{pet.info()}, "
                f"Breed: {pet.breed}, "
                f"Nature: {pet.nature}, "
                f"Mammal: {pet.mammal}"
            )