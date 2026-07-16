import sys
from string import punctuation


def main():
    '''
    Program takes a single string argument and displays
    the sums of its upper-case characters, lower-case characters,
    punctuation characters, digits, and spaces.
    '''


try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        try:
            text = ""
            while True:
                c = sys.stdin.read(1)
                if c == "":
                    break
                text += c
                if c == '\n':
                    break
        except KeyboardInterrupt as e:
            raise AssertionError("Program terminated by user") from e

    print(f"The text contains {len(text)} characters:")
    print(f"{sum(1 for c in text if c.isupper())} upper letters")
    print(f"{sum(1 for c in text if c.islower())} lower letters")
    print(f"{sum(1 for c in text if c in punctuation)} punctuation marks")
    print(f"{sum(1 for c in text if c.isspace())} spaces")
    print(f"{sum(1 for c in text if c.isdigit())} digits")

except AssertionError as e:
    print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()
