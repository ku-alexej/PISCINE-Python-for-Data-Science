from PIL import Image
from PIL import UnidentifiedImageError
import numpy as np

ERROR_PATH = "path must be a string"
ERROR_EMPTY_PATH = "path cannot be empty"
ERROR_FORMAT = "only JPG and JPEG formats are supported"


def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its shape and return its RGB pixel array.
    """

    try:
        assert isinstance(path, str), ERROR_PATH
        assert path.strip(), ERROR_EMPTY_PATH

        image = Image.open(path)
        assert image.format in ["JPEG", "JPG"], ERROR_FORMAT

        w, h = image.size

        left = w // 2 - 70
        top = h // 2 - 280
        right = left + 400
        bottom = top + 400
        image = image.crop((left, top, right, bottom))

        arr = np.array(image.convert("L"))

        arr_expand = np.expand_dims(arr, axis=-1)
        print("The shape of image is:", arr_expand.shape, "or", arr.shape)
        print(arr_expand)
        return arr

    except FileNotFoundError:
        print("Error: file not found")
    except PermissionError:
        print("Error: permission denied")
    except UnidentifiedImageError:
        print("Error: cannot identify image file")
    except IsADirectoryError:
        print("Error: path is a directory")
    except AssertionError as e:
        print(f"Error: {e}")
    except OSError:
        print("Error: corrupted image")
    except Exception as e:
        print(f"Error loading image: {e}")

    return None
