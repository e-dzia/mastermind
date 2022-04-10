import argparse
import datetime
import itertools

from players.player import Player
from mcts.enums import MCTSStrategy
from mcts.mcts_player import MCTSPlayer
from players.smart_player import SmartPlayer, SmartStrategy
from scripts.utils import decode_player_and_strategy
from simulator.color import Color
import logging
import numpy as np
import pandas as pd
from tqdm import tqdm

from simulator.game_code import Code
from settings import PROJECT_PATH


def main_experiments(player: Player=None, num_experiments=1):
    res_mean_list = []
    res_max_list = []
    for i in range(num_experiments):
        print(i)
        res_mean, res_max = main_experiments_all_codes(player)
        res_mean_list.append(res_mean)
        res_max_list.append(res_max)

    return np.mean(res_mean_list), max(res_max_list)


def main_experiments_all_codes(player: Player = None):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    colors = list(Color)
    colors.remove(Color.EMPTY)
    possible_codes = [p for p in itertools.product(colors, repeat=4)]

    if player is None:
        player = SmartPlayer(strategy=SmartStrategy.FIRST)

    rounds = []
    for possible_code in tqdm(possible_codes):

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


def main_experiments_smart(num_experiments: int=50):
    results = pd.DataFrame()
    res_mean, res_max = main_experiments(SmartPlayer(SmartStrategy.FIRST),
                                         num_experiments=1)
    results = results.append({'strategy': 'first', 'mean': res_mean,
                              'max': res_max}, ignore_index=True)
    print(results)

    res_mean, res_max = main_experiments(SmartPlayer(SmartStrategy.LAST),
                                         num_experiments=1)
    results = results.append({'strategy': 'last', 'mean': res_mean,
                              'max': res_max}, ignore_index=True)
    print(results)

    res_mean, res_max = main_experiments(SmartPlayer(SmartStrategy.RANDOM),
                                         num_experiments=num_experiments)
    results = results.append({'strategy': 'random',
                              'mean': res_mean,
                              'max': res_max}, ignore_index=True)
    print(results)

    results.to_csv(f'{PROJECT_PATH}/results/results_smart.csv')


def main_experiments_mcts(num_simulations: int=5000, num_experiments: int=5):
    results = pd.DataFrame()

    res_mean, res_max = main_experiments(
        MCTSPlayer(MCTSStrategy.MEAN_REWARD,
                   num_simulations=num_simulations),
        num_experiments=num_experiments)
    results = results.append({'strategy': 'mean_reward',
                              'num_simulations': num_simulations,
                              'mean': res_mean,
                              'max': res_max}, ignore_index=True)
    print(results)

    res_mean, res_max = main_experiments(
        MCTSPlayer(MCTSStrategy.GAMES_PERFORMED,
                   num_simulations=num_simulations),
        num_experiments=num_experiments)
    results = results.append({'strategy': 'games_performed',
                              'num_simulations': num_simulations,
                              'mean': res_mean,
                              'max': res_max}, ignore_index=True)
    print(results)

    results.to_csv(f'{PROJECT_PATH}/results/results_mcts_{num_simulations}.csv')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("player", help="Player to use, one of 'smart', 'mcts'")
    parser.add_argument("strategy",
                        help="Strategy to use, one of 'games_performed', 'mean_reward' (for 'mcst' player) or one of 'first', 'last', 'random' (for 'smart' player)")
    parser.add_argument("--num_simulations",
                        help="Number of simulations of the MCTS player, defaults to 5000",
                        required=False, default=5000, type=int)
    parser.add_argument("--num_experiments",
                        help="Number of experiments of non-deterministic strategies, defaults to 1",
                        required=False, default=1, type=int)
    args = parser.parse_args()

    start = datetime.datetime.now()

    if args.strategy != 'all':
        print(main_experiments(
            player=decode_player_and_strategy(args.player, args.strategy,
                                              args.num_simulations),
            num_experiments=args.num_experiments))
    elif args.player == 'smart' and args.strategy == 'all':
        main_experiments_smart(args.num_experiments)
    elif args.player == 'mcts' and args.strategy == 'all':
        main_experiments_mcts(args.num_simulations, args.num_experiments)
    else:
        raise Exception("Wrong parameters")

    end = datetime.datetime.now()
    print(f"Time: {end - start}")
