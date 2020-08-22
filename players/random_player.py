import random

from simulator.game_code import Code
from simulator.color import Color
from players.player import Player


class RandomPlayer(Player):
    def next_code(self, round=0):
        colors = list(Color)
        colors.remove(Color.EMPTY)
        code = Code(random.choice(colors), random.choice(colors),
                    random.choice(colors), random.choice(colors))
        self.code = code
        return self.code
