import datetime
import itertools
import os

from mcts.enums import MCTSStrategy
from mcts.mcts_player import MCTSPlayer
from players.player import Player
from players.enums import SmartStrategy
from players.smart_player import SmartPlayer, SmartStrategy
from scripts.utils import decode_player_and_strategy
from simulator.color import Color
import logging
import argparse

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("player", help="Player to use, one of 'smart', 'mcts'")
    parser.add_argument("strategy",
                        help="Strategy to use, one of 'games_performed', 'mean_reward' (for 'mcst' player) or one of 'first', 'last', 'random' (for 'smart' player)")
    parser.add_argument("--num_simulations",
                        help="Number of simulationd of the MCTS player, defaults to 1000",
                        required=False, default=1000, type=int)
    parser.add_argument("--code",
                        help="Code to play against",
                        required=False, default="5021", type=str)

    args = parser.parse_args()

    start = datetime.datetime.now()

    code = Code()
    code.set_from_string(args.code)

    if len(code.colors) != 4:
        for color in list(Color):
            color_str = str(color).replace('Color.', '')
            print(f"                    {color_str} = {color.value}")
        raise Exception(f"Code must be 4 digits of valid values")

    main_single(player=decode_player_and_strategy(args.player, args.strategy, args.num_simulations),
                code=code)

    end = datetime.datetime.now()
    print(f"Time: {end - start}")
