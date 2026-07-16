import numpy as np

ERROR_NOT_LIST = "family must be a list"
ERROR_NOT_2D_LIST = "family must be a 2D list"
ERROR_START_NOT_INT = "start must be an integer"
ERROR_END_NOT_INT = "end must be an integer"
ERROR_NOT_2D_ARRAY = "family must be a 2D array"
ERROR_ROWS_NOT_SAME_SIZE = "family rows must have the same size"


def slice_me(family: list, start: int, end: int) -> list:
    """
    Return a sliced 2D list from start to end (rows).
    """

    assert isinstance(family, list), ERROR_NOT_LIST
    assert len(family) > 0, ERROR_NOT_2D_LIST
    assert all(isinstance(row, list) for row in family), ERROR_NOT_2D_LIST
    assert isinstance(start, int), ERROR_START_NOT_INT
    assert isinstance(end, int), ERROR_END_NOT_INT
    row_length = len(family[0])
    assert all(len(row) == row_length for row in family), ERROR_ROWS_NOT_SAME_SIZE

    array = np.array(family)
    assert array.ndim == 2, ERROR_NOT_2D_ARRAY
    print("My shape is :", array.shape)

    new_array = array[start:end]
    print("My new shape is :", new_array.shape)

    return new_array.tolist()
