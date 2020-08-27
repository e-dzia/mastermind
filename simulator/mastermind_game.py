import random
import logging

from simulator.game_code import Code
from simulator.color import Color
from simulator.reward import Reward

logger = logging.getLogger(__name__)


class MastermindGame:
    def __init__(self, code: Code = None):
        if code is None:
            colors = list(Color)
            colors.remove(Color.EMPTY)
            self.code = Code(random.choice(colors), random.choice(colors),
                             random.choice(colors), random.choice(colors))
        else:
            self.code = code

        logger.info(self.code)
        # print(self.player)

    def play_round(self, player_code, num_round):
        won = False
        logger.info(player_code)
        same_color_and_spot = self.code.count_same_color_and_spot(player_code)
        same_color = self.code.count_same_color(player_code)
        logger.info(f"Good color and spot: {same_color_and_spot}, good color, "
                    f"wrong spot: {same_color}")
        points = self.code.evaluate(player_code, num_round + 1)
        logger.info(f"Points: {points}")
        if self.code == player_code:
            won = True
        return same_color, same_color_and_spot, points, won
