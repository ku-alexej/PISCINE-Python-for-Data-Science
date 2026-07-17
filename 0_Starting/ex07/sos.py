import sys


def main():
    '''
    The program takes a string as an argument and
    encodes it into Morse Code
    '''

    NESTED_MORSE = {
        ' ': '/ ',
        'A': '.- ',
        'B': '-... ',
        'C': '-.-. ',
        'D': '-.. ',
        'E': '. ',
        'F': '..-. ',
        'G': '--. ',
        'H': '.... ',
        'I': '.. ',
        'J': '.--- ',
        'K': '-.- ',
        'L': '.-.. ',
        'M': '-- ',
        'N': '-. ',
        'O': '--- ',
        'P': '.--. ',
        'Q': '--.- ',
        'R': '.-. ',
        'S': '... ',
        'T': '- ',
        'U': '..- ',
        'V': '...- ',
        'W': '.-- ',
        'X': '-..- ',
        'Y': '-.-- ',
        'Z': '--.. ',
        '0': '----- ',
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
    }

    try:
        assert len(sys.argv) == 2
        message = sys.argv[1]
        assert type(message) is str
        message = message.upper()
        assert all(c in NESTED_MORSE for c in message)

        print("".join(NESTED_MORSE[c] for c in message).rstrip())

    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
