from lab3.task3.apple import Apple
from lab3.task3.apple_tree import AppleTree
from lab3.task3.gardener import Gardener

if __name__ == '__main__':
    print("=== Створення кількох яблук ===")
    a1 = Apple(100)
    a2 = Apple(101)
    a2.grow()

    print("\n=== Довідка по всім яблукам ===")
    Gardener.apple_base()

    print("\n=== Створення дерева і садівника ===")
    tree = AppleTree(3)
    gardener = Gardener('Микола', tree)

    print("\n=== Спроба зібрати урожай (ще не час) ===")
    gardener.harvest()

    print("\n=== Догляд за деревом ===")
    while not tree.all_are_ripe():
        gardener.work()

    print("\n=== Збір врожаю ===")
    gardener.harvest()