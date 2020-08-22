import itertools
import os

from players.smart_player import SmartPlayer
from players.random_player import RandomPlayer
from simulator.color import Color
from simulator.game import Game
from players.user_player import UserPlayer
import logging
import numpy as np

from simulator.game_code import Code


def main_single():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    print("ready")

    game = Game(SmartPlayer(), Code(Color.ORANGE, Color.PURPLE,
                                    Color.ORANGE, Color.YELLOW))
    round = game.play_game(50)

    print(round)


def main_experiments():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    colors = list(Color)
    colors.remove(Color.EMPTY)
    possible_codes = [p for p in itertools.product(colors, repeat=4)]

    rounds = []
    for possible_code in possible_codes:
        # print(possible_code)
        game = Game(SmartPlayer(), Code(*possible_code))
        round = game.play_game(50)
        rounds.append(round)
    print(f"Mean: {np.mean(rounds)}")
    print(f"Max: {max(rounds)}")
    print(f"Min: {min(rounds)}")


def main_user():
    game = Game(UserPlayer())
    game.play_game()


if __name__ == "__main__":
    main_single()

