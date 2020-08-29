import datetime
import itertools
import os

from mcts.mcts_player import MCTSPlayer
from players.player import Player
from players.smart_player import SmartPlayer, SmartStrategy
from simulator.color import Color
from players.user_player import UserPlayer
import logging
import numpy as np
import pandas as pd

from simulator.game_code import Code


def main_single(player: Player, code: Code = None):
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    print("ready")

    if code is None:
        code = Code(Color.ORANGE, Color.PURPLE, Color.ORANGE, Color.YELLOW)

    if player is None:
        player = SmartPlayer()

    round = player.play_game(50, code)

    print(round + 1)


def main_experiments(player: Player):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    colors = list(Color)
    colors.remove(Color.EMPTY)
    possible_codes = [p for p in itertools.product(colors, repeat=4)]

    rounds = []
    for possible_code in possible_codes:
        # print(possible_code)
        code = Code(*possible_code)
        player = SmartPlayer(strategy=strategy)
        round = player.play_game(50, code)
        rounds.append(round + 1)
    print(f"Number of games: {len(rounds)}")
    print(f"Mean: {np.mean(rounds)}")
    print(f"Max: {max(rounds)}")
    print(f"Min: {min(rounds)}")
    return np.mean(rounds), max(rounds)


def main_user():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    player = UserPlayer()
    player.play_game()


def main_experiments_results():
    results = pd.DataFrame()
    res_mean, res_max = main_experiments(SmartStrategy.FIRST)
    results = results.append({'strategy': 'first', 'mean': res_mean,
                              'max': res_max}, ignore_index=True)

    print(results)

    res_mean, res_max = main_experiments(SmartStrategy.LAST)
    results = results.append({'strategy': 'last', 'mean': res_mean,
                              'max': res_max}, ignore_index=True)

    print(results)

    res_mean_list = []
    res_max_list = []
    for i in range(10):
        print(i)
        res_mean, res_max = main_experiments(SmartStrategy.RANDOM)
        res_mean_list.append(res_mean)
        res_max_list.append(res_max)

    results = results.append({'strategy': 'random',
                              'mean': np.mean(res_mean_list),
                              'max': max(res_max_list)}, ignore_index=True)

    print(results)

    results.to_csv('../results/results.csv')


if __name__ == "__main__":
    start = datetime.datetime.now()

    # main_experiments(player=SmartPlayer(Strategy.FIRST))
    # main_experiments(player=MCTSPlayer())
    # main_single(player=SmartPlayer(Strategy.FIRST), code=Code(Color.WHITE, Color.WHITE, Color.ORANGE, Color.YELLOW))
    main_single(player=MCTSPlayer(), code=Code(Color.PINK, Color.PURPLE, Color.WHITE, Color.RED))

    end = datetime.datetime.now()
    print(f"Time: {end - start}")
