class User:
    def __init__(
        self,
        first_name,
        last_name,
        email,
        username,
        newsletter_agreement,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.newsletter_agreement = newsletter_agreement
        self.login_attempts = 0  # пункт b)

    def describe_user(self):
        print(f"User full name: {self.first_name} {self.last_name}")

    def greeting_user(self):
        print(f"Hello, {self.username}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0