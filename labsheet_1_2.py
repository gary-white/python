import random


responses = ["correct", "too high", "too low"]


def respond_to_guess(g, n):
    return (g > n) - (g < n)


def lookup_response_string(r):
    return responses[r]


def main():
    number_of_guesses = 0
    n = random.randint(1, 100)

    while True:
        guess = int(input("Enter your guess: "))
        number_of_guesses += 1
        response = respond_to_guess(guess, n)
        if response == 0:
            break
        else:
            print(lookup_response_string(response))

    print("You guessed correctly after {} attempts.".format(number_of_guesses))


if __name__ == "__main__":
    main()
