from math import pi
from math import e


def compute_eulers_identity():
    return e ** (complex(0, 1) * pi)


def main():
    i = compute_eulers_identity()
    print(i)


if __name__ == "__main__":
    main()
