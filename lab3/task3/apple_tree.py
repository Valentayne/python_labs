from lab3.task3.apple import Apple


class AppleTree:
    def __init__(self, count):
        self.apples = [Apple(i + 1) for i in range(count)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
        count = len(self.apples)
        self.apples.clear()
        print(f"Зібрано {count} яблук!")
