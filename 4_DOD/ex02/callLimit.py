from typing import Any


def callLimit(limit: int):
    '''Decorator that limits the number of times a function can be called.'''

    count = 0

    def callLimiter(function):
        '''Returns a function that limits the number of
        times the original function can be called.'''

        def limit_function(*args: Any, **kwds: Any):
            '''Returns the result of the original function if
            the limit has not been reached.'''
            nonlocal count

            if count < limit:
                count += 1
                return function(*args, **kwds)

            print(f"Error: {function} call too many times")
            return

        return limit_function

    return callLimiter
