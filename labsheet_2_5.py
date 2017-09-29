class HangmanGame(object):
    def __init__(self, target_word):
        self.target_word = target_word
        self.total_number_of_guesses = 0
        self.number_of_correct_guesses = 0
        self.previous_guesses = set()
        self.found_letters = []

    def guess(self, letter):
        self.total_number_of_guesses += 1
        present = letter in self.target_word
        if present:
            self.found_letters.append(letter)
            self.number_of_correct_guesses += 1
        else:
            self.previous_guesses.add(letter)
        return self.get_found_word() == self.target_word

    def get_found_word(self):
        word_as_list_of_letters = list(self.target_word)
        i = 0
        for letter in word_as_list_of_letters:
            if letter not in self.found_letters:
                word_as_list_of_letters[i] = '_'
            i += 1
        return str(''.join(word_as_list_of_letters))

    def get_previous_guesses(self):
        return sorted(list(self.previous_guesses))

    def get_number_of_correct_guesses(self):
        return self.number_of_correct_guesses

    def get_total_number_of_guesses(self):
        return self.total_number_of_guesses


def main():
    game = HangmanGame('banana')
    correct = False
    while not correct and game.get_total_number_of_guesses() < 10:
        print('The word is: ' + game.get_found_word())
        print('You\'ve already correctly guessed {}'.format(game.get_number_of_correct_guesses()))
        print('You\'ve already incorrectly guessed the following letters:', game.get_previous_guesses())
        letter = input('Enter a letter: ')
        correct = game.guess(letter)
    if correct:
        print('Nice work! You found the word: ' + game.get_found_word())
    else:
        print('You ran out of guesses! You found: ' + game.get_found_word())


if __name__ == "__main__":
    main()


# todo room for improvement
# validate input
