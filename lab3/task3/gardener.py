from lab3.task3.apple import Apple
from lab3.task3.apple_tree import AppleTree


class Gardener:
    def __init__(self, name, tree: AppleTree):
        self.name = name
        self._tree = tree

    def work(self):
        self._tree.grow_all()
        print(f"{self.name} попрацював. Стан яблук: "
              f"{[str(a) for a in self._tree.apples]}")

    def harvest(self):
        if self._tree.all_are_ripe():
            print(f"{self.name} збирає врожай!")
            self._tree.give_away_all()
        else:
            print("Попередження: яблука ще не дозріли!")

    @staticmethod
    def apple_base():
        print("=== Довідка по яблуках ===")
        print(f"Всього яблук: {len(Apple._all_apples)}")
        for apple in Apple._all_apples:
            print(f"  {apple}")

