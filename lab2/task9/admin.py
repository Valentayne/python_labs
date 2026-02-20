from privilges import Privileges
from user import User

class Admin(User):
    def __init__(
        self,
        first_name,
        last_name,
        email,
        username,
        newsletter_agreement,
    ):
        super().__init__(
            first_name,
            last_name,
            email,
            username,
            newsletter_agreement,
        )
        self.priv = Privileges()