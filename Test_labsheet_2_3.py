import unittest
import random

from labsheet_2_3 import GuessingGame


class Tests(unittest.TestCase):
    def setUp(self):
        self.g = GuessingGame()

    @staticmethod
    def simulate_game_with_random_guesses(self):
        n = 1
        while self.g.guess(random.randint(1, 100)):
            n += 1
        return n

    @staticmethod
    def simulate_game_with_bisecting_guesses(self):
        n = 1
        lower_limit = 1
        upper_limit = 100
        guess = random.randint(1, 100)
        # print('='+str(self.g.target_number)+'=')
        # print('G: ' + str(guess))
        while True:
            response = self.g.guess(guess)
            # print('R: ' + str(response) + ' - {}:{}'.format(lower_limit, upper_limit))
            if not response:
                break
            if lower_limit == upper_limit:
                guess = lower_limit
                # print('G: ' + str(guess))
                continue
            if response == -1:
                lower_limit = guess + 1
                guess = guess + (upper_limit - guess) // 2
            else:
                upper_limit = guess - 1
                guess = guess - (guess - lower_limit) // 2
            # print('G: ' + str(guess))
            n += 1
        return n

    @staticmethod
    def simulate_game_with_enumerated_guesses(self):
        n = 1
        while self.g.guess(n):
            n += 1
        return n

    def test_simulate_many_games_with_random_guesses(self):
        n = 0
        for i in range(1, 10000):
            n = n + self.simulate_game_with_random_guesses(self)
        print('Random = {} '.format(n / 10000))

    def test_simulate_many_games_with_bisecting_guesses(self):
        n = 0
        for i in range(1, 10000):
            n = n + self.simulate_game_with_bisecting_guesses(self)
        print('Bisecting = {} '.format(n / 10000))

    def test_simulate_many_games_with_enumerated_guesses(self):
        n = 0
        for i in range(1, 10000):
            n = n + self.simulate_game_with_enumerated_guesses(self)
        print('Enumerated = {} '.format(n / 10000))

# todo think of alternative strategies for guessing the correct number quickly
