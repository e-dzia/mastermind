import logging

from simulator.game_code import Code
from simulator.mastermind_game import MastermindGame

logger = logging.getLogger(__name__)


class Player:
    def __init__(self):
        self.code = Code()
        self.history = []

    def reset(self):
        self.__init__()

    def next_code(self, round=0):
        return NotImplementedError

    def set_results(self, same_color_and_spot: int,
                    same_color: int):
        if same_color_and_spot >= 0 and same_color >= 0:
            self.history.append({'code': self.code,
                                 'same_color_and_spot': same_color_and_spot,
                                 'same_color': same_color})

    def __str__(self):
        return str(self.code)

    def play_game(self, rounds=10, code=None):
        game = MastermindGame(code)
        i = 0
        for i in range(rounds):
            logger.info(f"### ROUND {i + 1} ###")
            self.code = self.next_code(i)
            same_color, same_color_and_spot, points, won = (
                game.play_round(self.code, i))
            if won:
                break
            self.set_results(same_color_and_spot, same_color)
        logger.info(f"Good code: {self.code}")
        return i
