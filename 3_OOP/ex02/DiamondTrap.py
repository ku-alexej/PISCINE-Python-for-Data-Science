from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing a King character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for King class."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        """Sets the eyes attribute for the King."""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """Sets the hairs attribute for the King."""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """Returns the eyes attribute for the King."""
        return self.eyes

    def get_hairs(self) -> str:
        """Returns the hairs attribute for the King."""
        return self.hairs
