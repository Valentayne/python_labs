class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = [
                "Allowed to add message",
                "Allowed to delete users",
                "Allowed to ban users",
            ]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
