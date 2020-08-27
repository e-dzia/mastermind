import itertools
import os

from players.smart_player import SmartPlayer, Strategy
from simulator.color import Color
from players.user_player import UserPlayer
import logging
import numpy as np

from simulator.game_code import Code


def main_single():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    print("ready")

    code = Code(Color.ORANGE, Color.PURPLE, Color.ORANGE, Color.YELLOW)
    player = SmartPlayer()

    round = player.play_game(50, code)

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
        code = Code(*possible_code)
        player = SmartPlayer(strategy=Strategy.FIRST)
        round = player.play_game(50, code)
        rounds.append(round + 1)
    print(f"Number of games: {len(rounds)}")
    print(f"Mean: {np.mean(rounds)}")
    print(f"Max: {max(rounds)}")
    print(f"Min: {min(rounds)}")


def main_user():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    player = UserPlayer()
    player.play_game()


if __name__ == "__main__":
    main_experiments()
