class Privileges:
    def __init__(self, privileges=None):
        self.privileges = privileges if privileges is not None else []

    def show_privileges(self):
        return self.privileges