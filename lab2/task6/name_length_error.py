class NameLengthError(ValueError):
    def __init__(self, name):
        super().__init__(f"Name '{name}' is too short. Length must be at least 10.")