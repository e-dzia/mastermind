import random

from simulator.game_code import Code
from simulator.color import Color


class Player:
    def __init__(self):
        self.code = Code()
        self.history = []

    def next_code(self, round=0):
        return NotImplementedError

    def set_results(self, code: Code, same_color_and_spot: int,
                    same_color: int):
        self.history.append({'code': code,
                             'same_color_and_spot': same_color_and_spot,
                             'same_color': same_color})

    def __str__(self):
        return str(self.code)
