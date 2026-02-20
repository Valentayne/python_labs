class Apple:
    states = ['Відсутнє', 'Цвітіння', 'Зелене', 'Червоне']
    _all_apples = []

    def __init__(self, index):
        self._index = index
        self._state = Apple.states[0]
        Apple._all_apples.append(self)

    def grow(self):
        current = Apple.states.index(self._state)
        if current < len(Apple.states) - 1:
            self._state = Apple.states[current + 1]

    def is_ripe(self):
        return self._state == Apple.states[-1]

    def __str__(self):
        return f"Apple #{self._index}: {self._state}"
