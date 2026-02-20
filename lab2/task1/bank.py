"""Class Bank"""

class Bank:
    """Class Bank"""
    __balance = 0
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        """Method deposit"""
        self.__balance += amount

    def withdraw(self, amount):
        """Method withdraw"""
        if amount > self.__balance:
            return "you cannot withdraw more than you have"
        self.__balance -= amount
        return f"you have {self.__balance} after withdrawing {amount}"

    def checkout(self):
        """Method checkout"""
        return f"you have {self.__balance}"
