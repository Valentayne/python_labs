"""Coin class"""
import random

class Coin:
    """Coin class"""
    def __init__(self):
        self.site = random.choice(["heads", "tails"])

    def toss(self):
        """Toss coin"""
        self.site = random.choice(["heads", "tails"])
        return self.site