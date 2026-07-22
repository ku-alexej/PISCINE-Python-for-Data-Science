def square(x: int | float) -> int | float:
    '''Returns the square of a number.'''
    return x ** 2


def pow(x: int | float) -> int | float:
    '''Returns the power of a number.'''
    return x ** x


def outer(x: int | float, function) -> object:
    '''Returns an object that when called returns the result
    of the arguments calculation'''

    count = 0

    def inner() -> float:
        '''Returns the result of the arguments calculation'''
        nonlocal count
        count = function(x) if count == 0 else function(count)
        return count

    return inner
