import argparse
import datetime
import itertools

from players.player import Player
from players.smart_player import SmartPlayer, SmartStrategy
from scripts.utils import decode_player_and_strategy
from simulator.color import Color
import logging
import numpy as np
import pandas as pd

from simulator.game_code import Code
from settings import PROJECT_PATH


def main_experiments(player: Player = None):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    colors = list(Color)
    colors.remove(Color.EMPTY)
    possible_codes = [p for p in itertools.product(colors, repeat=4)]

    if player is None:
        player = SmartPlayer(strategy=SmartStrategy.FIRST)

    rounds = []
    for possible_code in possible_codes:
        start = datetime.datetime.now()

        # print(possible_code)
        code = Code(*possible_code)
        player.reset()
        num_round = player.play_game(rounds=50, code=code)
        rounds.append(num_round + 1)

        end = datetime.datetime.now()
        # print(f"Code: {possible_code}, time: {end - start}, rounds: {num_round + 1}")
    print(f"Number of games: {len(rounds)}")
    print(f"Mean: {np.mean(rounds)}")
    print(f"Max: {max(rounds)}")
    print(f"Min: {min(rounds)}")
    return np.mean(rounds), max(rounds)


def main_experiments_results():
    results = pd.DataFrame()
    res_mean, res_max = main_experiments(SmartPlayer(SmartStrategy.FIRST))
    results = results.append({'strategy': 'first', 'mean': res_mean,
                              'max': res_max}, ignore_index=True)

    print(results)

    res_mean, res_max = main_experiments(SmartPlayer(SmartStrategy.LAST))
    results = results.append({'strategy': 'last', 'mean': res_mean,
                              'max': res_max}, ignore_index=True)

    print(results)

    res_mean_list = []
    res_max_list = []
    for i in range(50):
        print(i)
        res_mean, res_max = main_experiments(SmartPlayer(SmartStrategy.RANDOM))
        res_mean_list.append(res_mean)
        res_max_list.append(res_max)

    results = results.append({'strategy': 'random',
                              'mean': np.mean(res_mean_list),
                              'max': max(res_max_list)}, ignore_index=True)

    print(results)

    results.to_csv(f'{PROJECT_PATH}/results/results.csv')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("player", help="Player to use, one of 'smart', 'mcts'")
    parser.add_argument("strategy",
                        help="Strategy to use, one of 'games_performed', 'mean_reward' (for 'mcst' player) or one of 'first', 'last', 'random' (for 'smart' player)")
    parser.add_argument("--num_simulations",
                        help="Number of simulationd of the MCTS player, defaults to 1000",
                        required=False, default=1000, type=int)
    args = parser.parse_args()

    start = datetime.datetime.now()

    if args.strategy != 'all':
        main_experiments(player=decode_player_and_strategy(args.player, args.strategy, args.num_simulations))
    elif args.player == 'smart' and args.strategy == 'all':
        main_experiments_results()
    else:
        raise Exception("Wrong parameters")

    end = datetime.datetime.now()
    print(f"Time: {end - start}")
