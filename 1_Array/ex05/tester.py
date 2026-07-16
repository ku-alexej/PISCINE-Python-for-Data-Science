from load_image import ft_load
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_green
from pimp_image import ft_blue
from pimp_image import ft_grey
from matplotlib import pyplot as plt

try:
    array = ft_load("landscape.jpg")
    plt.imshow(ft_invert(array))
    plt.show()
    plt.imshow(ft_red(array))
    plt.show()
    plt.imshow(ft_green(array))
    plt.show()
    plt.imshow(ft_blue(array))
    plt.show()
    plt.imshow(ft_grey(array))
    plt.show()
    print(ft_invert.__doc__)

except Exception as e:
    print(f"Error: {e}")
