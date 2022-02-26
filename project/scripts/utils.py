from mcts.enums import MCTSStrategy
from mcts.mcts_player import MCTSPlayer
from players.enums import SmartStrategy
from players.player import Player
from players.smart_player import SmartPlayer


def decode_player_and_strategy(player_arg: str, strategy_arg: str, num_simulations: int=1000) -> Player:
    if player_arg.lower() not in ['smart', 'mcts']:
        raise Exception(f'Wrong player - {player_arg}')
    if player_arg.lower() == 'smart':
        if strategy_arg.lower() not in ['first', 'last', 'random']:
            raise Exception(f'Wrong strategy for player SMART - {strategy_arg}')
        return SmartPlayer(SmartStrategy[strategy_arg.upper()])
    elif player_arg.lower() == 'mcts':
        if strategy_arg.lower() not in ['games_performed', 'mean_reward']:
            raise Exception(f'Wrong strategy for player MCST - {strategy_arg}')
        return MCTSPlayer(MCTSStrategy[strategy_arg.upper()], num_simulations=num_simulations)
