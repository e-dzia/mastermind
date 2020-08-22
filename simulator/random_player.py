import random

from simulator.code import Code
from simulator.color import Color
from simulator.player import Player


class RandomPlayer(Player):
    def next_code(self):
        colors = list(Color)
        colors.remove(Color.EMPTY)
        code = Code(random.choice(colors), random.choice(colors),
                    random.choice(colors), random.choice(colors))
        self.code = code
        return self.code
