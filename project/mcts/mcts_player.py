import random

from mcts.enums import MCTSStrategy
from mcts.mcts_tree import MCTSTree
from players.smart_player import SmartPlayer
from simulator.color import Color
from simulator.game_code import Code


class MCTSPlayer(SmartPlayer):
    def __init__(self, strategy: MCTSStrategy = MCTSStrategy.GAMES_PERFORMED,
                 num_simulations=5000):
        super().__init__()
        self.tree = None
        self.strategy = strategy
        self.num_simulations = num_simulations

    def reset(self):
        self.__init__(self.strategy, self.num_simulations)

    def next_code(self, round=0):
        if len(self.history) == 0:
            # top 10 codes for 100 000 simulations for both of the strategies
            # (20 codes total)
            self.code = random.choice([
                Code(Color.ORANGE, Color.PINK, Color.WHITE, Color.YELLOW),
                Code(Color.PURPLE, Color.WHITE, Color.PINK, Color.PINK),
                Code(Color.PURPLE, Color.ORANGE, Color.RED, Color.ORANGE),
                Code(Color.RED, Color.PINK, Color.YELLOW, Color.RED),
                Code(Color.WHITE, Color.PINK, Color.ORANGE, Color.ORANGE),
                Code(Color.YELLOW, Color.RED, Color.ORANGE, Color.YELLOW),
                Code(Color.WHITE, Color.YELLOW, Color.YELLOW, Color.ORANGE),
                Code(Color.WHITE, Color.ORANGE, Color.PINK, Color.RED),
                Code(Color.RED, Color.RED, Color.RED, Color.PURPLE),
                Code(Color.WHITE, Color.ORANGE, Color.YELLOW, Color.YELLOW),
                Code(Color.RED, Color.PURPLE, Color.PINK, Color.PURPLE),
                Code(Color.WHITE, Color.WHITE, Color.ORANGE, Color.ORANGE),
                Code(Color.PINK, Color.PINK, Color.YELLOW, Color.RED),
                Code(Color.RED, Color.PINK, Color.RED, Color.RED),
                Code(Color.PINK, Color.WHITE, Color.PINK, Color.RED),
                Code(Color.PINK, Color.PURPLE, Color.PINK, Color.YELLOW),
                Code(Color.PURPLE, Color.PINK, Color.ORANGE, Color.YELLOW),
                Code(Color.WHITE, Color.PURPLE, Color.PINK, Color.ORANGE),
                Code(Color.ORANGE, Color.PINK, Color.ORANGE, Color.RED),
                Code(Color.YELLOW, Color.RED, Color.PINK, Color.PINK),
            ])
            return self.code
        self.possible_codes.update(self.history[-1])
        self.tree = MCTSTree(self.code, self.possible_codes)
        self.tree.build_tree(num_simulations=self.num_simulations)
        self.code = self.tree.get_best_move(self.strategy)
        return self.code
