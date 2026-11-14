def factorial(n):
    """Return the factorial of a non-negative integer recursively."""
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n * factorial(n - 1)


def main():
    try:
        number = int(input("Enter an integer: "))

        if number < 0:
            print("Error: Negative numbers are invalid attempts.")
            return

        result = factorial(number)

        # Tuple structure: (factorial result, string identifier, input as float)
        output = (result, "factorial", float(number))

        print(f"Factorial of {number} = {result}")
        print(f"Output tuple: {output}")

    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()
