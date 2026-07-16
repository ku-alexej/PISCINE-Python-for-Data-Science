import numpy as np

ERROR_H_NOT_LIST = "height must be lists"
ERROR_W_NOT_LIST = "weight must be lists"
ERROR_BMI_NOT_LIST = "bmi must be a list"
ERROR_NOT_SAME_SIZE = "height and weight must have the same size"
ERROR_H_NOT_POSITIVE = "height must be bigger than 0"
ERROR_W_NOT_POSITIVE = "weight must be bigger than 0"
ERROR_H_DATA_TYPE = "height must be int or float"
ERROR_W_DATA_TYPE = "weight must be int or float"
ERROR_BMI_DATA_TYPE = "bmi must be int or float"
ERROR_LIMIT_DATA_TYPE = "limit must be an int"


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Compute BMI values from height and weight lists."""

    assert isinstance(height, list), ERROR_H_NOT_LIST
    assert isinstance(weight, list), ERROR_W_NOT_LIST
    assert len(height) == len(weight), ERROR_NOT_SAME_SIZE
    assert all(isinstance(x, (int, float)) for x in height), ERROR_H_DATA_TYPE
    assert all(isinstance(x, (int, float)) for x in weight), ERROR_W_DATA_TYPE

    height_array = np.array(height, dtype=float)
    weight_array = np.array(weight, dtype=float)

    assert np.all(height_array > 0), ERROR_H_NOT_POSITIVE
    assert np.all(weight_array > 0), ERROR_W_NOT_POSITIVE

    bmi = weight_array / np.square(height_array)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list indicating whether each BMI value is above the limit."""

    assert isinstance(bmi, list), ERROR_BMI_NOT_LIST
    assert isinstance(limit, int), ERROR_LIMIT_DATA_TYPE
    assert all(isinstance(x, (int, float)) for x in bmi), ERROR_BMI_DATA_TYPE

    bmi_array = np.array(bmi, dtype=float)

    return (bmi_array > limit).tolist()
