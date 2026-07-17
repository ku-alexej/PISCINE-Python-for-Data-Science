import random
from ft_filter import ft_filter


print(filter.__doc__)
print(ft_filter.__doc__)

lst_int = [random.randint(0, 100) for _ in range(20)]

print(type(ft_filter(lambda x: x % 2 == 0, lst_int)))
print(type(filter(lambda x: x % 2 == 0, lst_int)))

print(list(ft_filter(None, lst_int)))
print(list(filter(None, lst_int)))


lst_items = [
    1,
    0,
    "fox",
    "",
    "carrot",
    None
]

print(list(ft_filter(None, lst_items)))
print(list(filter(None, lst_items)))

try:
    print(list(ft_filter(10, lst_items)))
except TypeError as e:
    print(f"TypeError: {str(e)}")

try:
    print(list(filter(10, lst_items)))
except TypeError as e:
    print(f"TypeError: {str(e)}")

lst_wrong = [
    10,
    3.14,
    True,
    False,
    None,
    object(),
    5 + 2j,
]

try:
    print(list(ft_filter(lambda x: x > 5, lst_wrong)))
except TypeError as e:
    print(f"TypeError: {str(e)}")

try:
    print(list(filter(lambda x: x > 5, lst_wrong)))
except TypeError as e:
    print(f"TypeError: {str(e)}")
