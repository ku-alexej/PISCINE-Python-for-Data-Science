import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Return a sliced 2D list from start to end (rows).
    """

    assert isinstance(family, list), \
        "family must be a list"
    assert len(family) > 0, \
        "family must be a 2D list"
    assert all(isinstance(row, list) for row in family), \
        "family must be a 2D list"
    assert isinstance(start, int), \
        "start must be an integer"
    assert isinstance(end, int), \
        "end must be an integer"
    row_length = len(family[0])
    assert all(len(row) == row_length for row in family), \
        "family rows must have the same size"

    array = np.array(family)
    assert array.ndim == 2, \
        "family must be a 2D array"
    print("My shape is :", array.shape)

    new_array = array[start:end]
    print("My new shape is :", new_array.shape)

    return new_array.tolist()
