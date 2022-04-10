import argparse

from scripts.utils import decode_player_and_strategy


def run_helper(player):
    game_won = False
    while not game_won:
        code = player.next_code()
        print("Next code to use:", code)
        same_color_and_spot = int(input("Set results: same color and spot = "))
        same_color = int(input("Set results: same color = "))
        if same_color_and_spot == 4:
            game_won = True
        player.set_results(same_color_and_spot, same_color)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("player", help="Player to use, one of 'smart', 'mcts'")
    parser.add_argument("strategy",
                        help="Strategy to use, one of 'games_performed', 'mean_reward' (for 'mcst' player) or one of 'first', 'last', 'random' (for 'smart' player)")
    parser.add_argument("--num_simulations",
                        help="Number of simulations of the MCTS player, defaults to 10000",
                        required=False, default=10000, type=int)
    args = parser.parse_args()

    player = decode_player_and_strategy(args.player, args.strategy, args.num_simulations)
    run_helper(player)
