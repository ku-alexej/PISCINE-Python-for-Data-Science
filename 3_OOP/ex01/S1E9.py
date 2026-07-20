from abc import ABC, abstractmethod


class Character(ABC):
    """Representing a character in the Game of Thrones universe."""

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Character class."""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Die method for Character class sets the is_alive attribute to False."""
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Stark class."""
        super().__init__(first_name, is_alive)
