class calculator:
    """A class that represents a simple calculator."""

    def __init__(self, lst: list) -> None:
        if not isinstance(lst, list):
            raise TypeError("Input must be a list.")
        self.vector = [float(i) for i in lst]

    def __add__(self, object) -> None:
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        try:
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            raise ZeroDivisionError("Division by zero is not allowed.") from e
