import operator
from functools import reduce


def compute_factorial(n):
    numbers = list(range(366 - n, 366))

    return reduce(operator.mul, numbers)


def compute_probability(n):
    if n < 2:
        return 0.0

    p_not_a = ((1.0 / 365.0) ** n) * compute_factorial(n)

    return 1.0 - p_not_a


def main():
    p = compute_probability(23)
    print(p)


if __name__ == "__main__":
    main()


# todo this was really about populating a list with random numbers and producing statistics
