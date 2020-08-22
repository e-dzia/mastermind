import random

from simulator.code import Code
from simulator.color import Color
from simulator.player import Player
from simulator.random_player import RandomPlayer
from simulator.reward import Reward
from simulator.user_player import UserPlayer


class Game:
    def __init__(self, player: Player = RandomPlayer()):
        self.player = player
        colors = list(Color)
        colors.remove(Color.EMPTY)
        self.code = Code(random.choice(colors), random.choice(colors),
                         random.choice(colors), random.choice(colors))

        print(self.code)
        # print(self.player)

    def round(self):
        player_code = self.player.next_code()
        print(player_code)
        same_color_and_spot = self.code.count_same_color_and_spot(player_code)
        same_color = self.code.count_same_color(player_code)
        print(f"Good color and spot: {same_color_and_spot}, good color, "
              f"wrong spot: {same_color}")
        points = self.code.evaluate(player_code)
        print(f"Points: {points}")
        if points == Reward.WIN.value:
            return True

    def play_game(self, rounds=10):
        for i in range(rounds):
            end = self.round()
            if end:
                break
