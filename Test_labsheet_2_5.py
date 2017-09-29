import string
import unittest

from labsheet_2_5 import HangmanGame


class Tests(unittest.TestCase):
    def setUp(self):
        self.game = HangmanGame('banana')

    def blank_word(self):
        return len(self.game.get_found_word()) * '_'

    def test_game_initial_state(self):
        self.assertEqual(self.blank_word(), self.game.get_found_word())
        self.assertListEqual([], self.game.get_previous_guesses())
        self.assertEqual(0, self.game.get_number_of_correct_guesses())
        # test the output
        self.assertEqual("[]", str(self.game.get_previous_guesses()))

    def test_game_after_one_incorrect_guess(self):
        self.assertFalse(self.game.guess('x'))
        self.assertEqual(self.blank_word(), self.game.get_found_word())
        self.assertListEqual(['x'], self.game.get_previous_guesses())
        # test the output
        self.assertEqual("['x']", str(self.game.get_previous_guesses()))

    def test_game_after_two_incorrect_guesses(self):
        self.assertFalse(self.game.guess('x'))
        self.assertFalse(self.game.guess('y'))
        self.assertEqual(self.blank_word(), self.game.get_found_word())
        self.assertListEqual(['x', 'y'], self.game.get_previous_guesses())

    def test_game_after_two_duplicate_incorrect_guesses(self):
        self.assertFalse(self.game.guess('x'))
        self.assertFalse(self.game.guess('x'))
        self.assertEqual(self.blank_word(), self.game.get_found_word())
        self.assertListEqual(['x'], self.game.get_previous_guesses())

    def test_game_after_one_correct_guess(self):
        self.assertFalse(self.game.guess('b'))
        self.assertEqual('b_____', self.game.get_found_word())
        self.assertEqual(1, self.game.get_number_of_correct_guesses())
        self.assertListEqual([], self.game.get_previous_guesses())

    def test_game_after_two_correct_guesses(self):
        self.assertFalse(self.game.guess('b'))
        self.assertFalse(self.game.guess('a'))
        self.assertEqual('ba_a_a', self.game.get_found_word())
        self.assertEqual(2, self.game.get_number_of_correct_guesses())
        self.assertListEqual([], self.game.get_previous_guesses())

    def test_game_after_three_correct_guesses(self):
        self.assertFalse(self.game.guess('b'))
        self.assertFalse(self.game.guess('a'))
        # We're done here
        self.assertTrue(self.game.guess('n'))
        self.assertEqual('banana', self.game.get_found_word())
        self.assertEqual(3, self.game.get_number_of_correct_guesses())
        self.assertListEqual([], self.game.get_previous_guesses())

    def test_game_after_one_incorrect_and_three_correct_guesses(self):
        self.assertFalse(self.game.guess('x'))
        self.assertListEqual(['x'], self.game.get_previous_guesses())
        self.assertFalse(self.game.guess('b'))
        self.assertFalse(self.game.guess('a'))
        # We're done here
        self.assertTrue(self.game.guess('n'))
        self.assertEqual('banana', self.game.get_found_word())
        self.assertEqual(3, self.game.get_number_of_correct_guesses())
        self.assertListEqual(['x'], self.game.get_previous_guesses())

    def simulate_game(self, target_word):
        self.game = HangmanGame(target_word)
        guesses = tuple(string.ascii_lowercase)
        i, correct = 0, False
        while not correct and self.game.get_total_number_of_guesses() < 10:
            print('Try ' + guesses[i])
            correct = self.game.guess(guesses[i])
            print(self.game.get_found_word())
            print(self.game.get_previous_guesses())
            print(self.game.get_number_of_correct_guesses())
            i += 1
        if correct:
            print('Nice work! You found the word: ' + self.game.get_found_word())
        else:
            print('You ran out of guesses! You found: ' + self.game.get_found_word())

    def test_simulate_game_with_under_10_guesses(self):
        self.simulate_game('abba')

    def test_simulate_game_with_exactly_10_guesses(self):
        self.simulate_game('jag')

    def test_simulate_game_with_over_10_guesses(self):
        self.simulate_game('xylophone')
