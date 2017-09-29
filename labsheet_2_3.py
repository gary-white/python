import random


class GuessingGame(object):

    target_number = 0

    def __init__(self) -> None:
        super().__init__()
        self.target_number = random.randint(1, 100)

    def guess(self, n):
        return (n > self.target_number) - (n < self.target_number)
