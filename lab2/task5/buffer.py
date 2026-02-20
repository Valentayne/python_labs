"""Buffer class"""
class Buffer:
    """Buffer class"""
    def __init__(self):
        self.data = []

    def add(self, *a):
        """Add an element to the buffer"""
        self.data.extend(a)

        while len(self.data) >= 5:
            five = self.data[:5]
            print(sum(five))
            self.data = self.data[5:]

    def get_current_part(self):
        return self.data
