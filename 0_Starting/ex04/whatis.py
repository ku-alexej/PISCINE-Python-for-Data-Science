import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    number = int(sys.argv[1])

    print("I'm Even." if number % 2 == 0 else "I'm Odd.")

except IndexError:
    pass

except ValueError:
    print("AssertionError: argument is not an integer")

except AssertionError as e:
    print(f"AssertionError: {e}")
