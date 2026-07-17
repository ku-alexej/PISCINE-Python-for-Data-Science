from typing import Iterable, Iterator, Optional


def ft_filter(function: Optional[callable], iterable: Iterable) -> Iterator:
    '''
    Return an iterator yielding those items of iterable
    for which function(item) is true. If function is None,
    return the items that are true.
    '''

    return [x for x in iterable
            if (function is None and x)
            or (function is not None and function(x))]
