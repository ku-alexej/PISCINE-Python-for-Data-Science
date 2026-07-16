from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    Load an image, extract a 400x400 pixel zoom region, and display it.
    """
    try:
        image = ft_load("animal.jpeg")

        if image is None:
            return

        arr = np.array(image)

        print(arr)

        w, h = image.size

        if w < 400 or h < 400:
            print("Image too small")
            return

        x = w // 2 - 70
        y = h // 2 - 280

        gray = image.convert("L")
        arr = np.array(gray)
        arr = arr[y:y + 400, x:x + 400]
        arr = arr[:, :, np.newaxis]

        print(f"New shape after slicing: {arr.shape}")
        print(arr)

        plt.imshow(arr, cmap="gray")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
