from PIL import Image
from PIL import UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> Image:
    """
    Load an image, print its shape and return its RGB pixel array.
    """

    try:
        assert isinstance(path, str), \
            "path must be a string"
        assert path.strip(), \
            "path cannot be empty"

        image = Image.open(path)
        assert image.format in ["JPEG", "JPG"], \
            "only JPG and JPEG formats are supported"

        image = image.convert("RGB")
        array = np.array(image)
        print("The shape of image is:", array.shape)

        return image

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
