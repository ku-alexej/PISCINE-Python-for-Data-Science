import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Generates a random string of 15 lowercase letters.'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    '''Data class representing a studentwith attributes for
    name, surname, active status, login, and a unique ID.'''

    name: str
    surname: str
    active: bool = field(default=True)
    # active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        '''Validates attributes and generates the login.'''
        self.login = f"{self.name[0]}{self.surname}"
