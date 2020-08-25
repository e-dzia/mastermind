import logging
import random

from simulator.mastermind_game import MastermindGame
from simulator.game_code import Code
from simulator.color import Color


logger = logging.getLogger(__name__)


class Player:
    def __init__(self):
        self.code = Code()
        self.history = []

    def next_code(self, round=0):
        return NotImplementedError

    def set_results(self, same_color_and_spot: int,
                    same_color: int):
        self.history.append({'code': self.code,
                             'same_color_and_spot': same_color_and_spot,
                             'same_color': same_color})

    def __str__(self):
        return str(self.code)

    def play_game(self, rounds=10, code=None):
        game = MastermindGame(code)
        i = 0
        for i in range(rounds):
            logger.info(f"### ROUND {i} ###")
            self.code = self.next_code(i)
            same_color, same_color_and_spot, points, won = game.play_round(self.code)
            if won:
                break
            self.set_results(same_color_and_spot, same_color)
        logger.info(f"Good code: {self.code}")
        return i
