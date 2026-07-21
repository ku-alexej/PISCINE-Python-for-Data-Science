import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Compute BMI values from height and weight lists."""

    assert isinstance(height, list), \
        "height must be lists"
    assert isinstance(weight, list), \
        "weight must be lists"
    assert len(height) == len(weight), \
        "height and weight must have the same size"
    assert all(isinstance(x, (int, float)) for x in height), \
        "height must be int or float"
    assert all(isinstance(x, (int, float)) for x in weight), \
        "weight must be int or float"

    height_array = np.array(height, dtype=float)
    weight_array = np.array(weight, dtype=float)

    assert np.all(height_array > 0), \
        "height must be bigger than 0"
    assert np.all(weight_array > 0), \
        "weight must be bigger than 0"

    bmi = weight_array / np.square(height_array)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list indicating whether each BMI value is above the limit."""

    assert isinstance(bmi, list), \
        "bmi must be a list"
    assert isinstance(limit, int), \
        "limit must be an int"
    assert all(isinstance(x, (int, float)) for x in bmi), \
        "bmi must be int or float"

    bmi_array = np.array(bmi, dtype=float)

    return (bmi_array > limit).tolist()
