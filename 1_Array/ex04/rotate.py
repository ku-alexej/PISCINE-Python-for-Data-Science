from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    Load an image, extract a 400x400 pixel zoom region, and display it.
    """
    try:
        arr = ft_load("animal.jpeg")

        if arr is None:
            return

        arr = arr.squeeze()

        h, w = arr.shape
        rotated = np.zeros((w, h), dtype=arr.dtype)

        for i in range(h):
            for j in range(w):
                rotated[-j][i] = arr[i][-j]

        print(f"New shape after Transpose: {rotated.shape}")
        print(rotated)

        plt.imshow(rotated, cmap="gray")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
