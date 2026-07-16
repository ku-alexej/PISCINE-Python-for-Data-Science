import numpy as np


def ft_invert(array) -> np.ndarray:
    '''
    Invert the colors of an RGB image represented as a NumPy array.
    Allowed operators: = + - *
    '''
    result = array.copy()
    result = 255 - result

    return result


def ft_red(array) -> np.ndarray:
    '''
    Extract the red channel from an RGB image represented as a NumPy array.
    Allowed operators: = *
    '''
    result = array.copy()

    result[:, :, 1] = result[:, :, 1] * 0
    result[:, :, 2] = result[:, :, 2] * 0

    return result


def ft_green(array) -> np.ndarray:
    '''
    Extract the green channel from an RGB image represented as a NumPy array.
    Allowed operators: = -
    '''
    result = array.copy()

    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]

    return result


def ft_blue(array) -> np.ndarray:
    '''
    Extract the blue channel from an RGB image represented as a NumPy array.
    Allowed operators: =
    '''
    result = array.copy()

    result = ft_green(ft_red(result))
    result[:, :, 2] = array[:, :, 2]

    return result


def ft_grey(array) -> np.ndarray:
    '''
    Convert an RGB image represented as a NumPy array to grayscale.
    Allowed operators: = /
    '''
    result = array.copy()

    red = ft_red(array)
    green = ft_green(array)
    blue = ft_blue(array)

    stacked = np.array([red[:, :, 0], green[:, :, 1], blue[:, :, 2]])
    grey = stacked.mean(axis=0)

    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey

    return result
