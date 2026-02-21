from lab4.task2.user import User
from lab4.task2.privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, email, nickname, newsletter=False, privileges=None):
        super().__init__(first_name, last_name, email, nickname, newsletter)
        self.priv = Privileges(privileges if privileges is not None else [
            "Allowed to add message",
            "Allowed to delete users",
            "Allowed to ban users"
        ])

    def show_privileges(self):
        return self.priv.show_privileges()