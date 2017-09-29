def describe_number_size(n):
    description = ""
    if n < 10:
        description = "small"
    elif n < 20:
        description = "medium"
    elif n > 20:
        description = "large"

    return description


def describe_number_parity(n):
    return "even" if n % 2 == 0 else "odd"


def main():
    while True:
        try:
            a_number = int(input("Please enter a number: "))
            print("This number is " + describe_number_size(a_number) + ", and it's " + describe_number_parity(
                a_number) + ".")
            break
        except ValueError:
            print("That's not a valid number. Try again..")


if __name__ == "__main__":
    main()
