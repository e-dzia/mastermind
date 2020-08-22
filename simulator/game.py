import random
import logging

from simulator.game_code import Code
from simulator.color import Color
from players.player import Player
from players.random_player import RandomPlayer
from simulator.reward import Reward


logger = logging.getLogger(__name__)


class Game:
    def __init__(self, player: Player = RandomPlayer(), code: Code = None):
        self.player = player
        if code is None:
            colors = list(Color)
            colors.remove(Color.EMPTY)
            self.code = Code(random.choice(colors), random.choice(colors),
                             random.choice(colors), random.choice(colors))
        else:
            self.code = code

        logger.info(self.code)
        # print(self.player)

    def round(self, round_number):
        player_code = self.player.next_code(round_number)
        logger.info(player_code)
        same_color_and_spot = self.code.count_same_color_and_spot(player_code)
        same_color = self.code.count_same_color(player_code)
        logger.info(f"Good color and spot: {same_color_and_spot}, good color, "
              f"wrong spot: {same_color}")
        self.player.set_results(player_code, same_color_and_spot, same_color)
        points = self.code.evaluate(player_code)
        logger.info(f"Points: {points}")
        if points == Reward.WIN.value:
            return True

    def play_game(self, rounds=10):
        i = 0
        for i in range(rounds):
            logger.info(f"### ROUND {i} ###")
            end = self.round(i)
            if end:
                break
        logger.info(f"Good code: {self.code}")
        return i
