import sys
from ft_filter import ft_filter


def main():
    '''
        The program outputs a list of words from S
        that have a length greater than N.
    '''
    try:
        assert len(sys.argv) == 3

        S = sys.argv[1]
        N = sys.argv[2]

        assert type(S) is str
        assert N.isdigit()

        N = int(N)
        words = S.split(" ")

        result = list(ft_filter(lambda w: len(w) > N, [w for w in words]))
        print(result)

    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
