from typing import Any


def _print_mean(lst: list) -> None:
    '''Prints the mean of a list of numbers.'''
    try:
        mean = sum(lst) / len(lst)
        print(f"mean : {mean:.1f}")
    except ZeroDivisionError:
        print("ERROR")


def _print_median(lst: list) -> None:
    '''Prints the median of a list of numbers.'''
    try:
        sorted_lst = sorted(lst)
        n = len(sorted_lst)
        if n % 2 == 0:
            median = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
        else:
            median = sorted_lst[n // 2]
        print(f"median : {median}")
    except IndexError:
        print("ERROR")


def _print_quartile(lst: list) -> None:
    '''Prints the first and third quartiles of a list of numbers.'''
    try:
        sorted_lst = sorted(lst)
        n = len(sorted_lst)
        q1 = sorted_lst[n // 4]
        q3 = sorted_lst[3 * n // 4]
        print(f"quartile : [{q1:.1f}, {q3:.1f}]")
    except IndexError:
        print("ERROR")


def _print_std(lst: list) -> None:
    '''Prints the standard deviation of a list of numbers.'''
    try:
        mean = sum(lst) / len(lst)
        variance = sum((x - mean) ** 2 for x in lst) / len(lst)
        std_dev = variance ** 0.5
        print(f"std : {std_dev}")
    except ZeroDivisionError:
        print("ERROR")


def _print_var(lst: list) -> None:
    '''Prints the variance of a list of numbers.'''
    try:
        mean = sum(lst) / len(lst)
        variance = sum((x - mean) ** 2 for x in lst) / len(lst)
        print(f"var : {variance}")
    except ZeroDivisionError:
        print("ERROR")


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    '''Prints statistics for list of numbers according to the commands.'''

    try:
        lst = list(args)
        cmds = list(kwargs.values())

        for cmd in cmds:
            if cmd == "mean":
                _print_mean(lst)
            elif cmd == "median":
                _print_median(lst)
            elif cmd == "quartile":
                _print_quartile(lst)
            elif cmd == "std":
                _print_std(lst)
            elif cmd == "var":
                _print_var(lst)
            else:
                pass

    except Exception:
        print("ERROR")
