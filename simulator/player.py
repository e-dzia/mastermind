import random

from simulator.code import Code
from simulator.color import Color


class Player:
    def __init__(self):
        self.code = Code()

    def next_code(self):
        return NotImplementedError

    def __str__(self):
        return str(self.code)
