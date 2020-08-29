from mcts.enums import MCTSStrategy
from mcts.mcts_tree import MCTSTree
from players.smart_player import SmartPlayer


class MCTSPlayer(SmartPlayer):
    def __init__(self, strategy: MCTSStrategy = MCTSStrategy.GAMES_PERFORMED):
        super().__init__()
        self.tree = None
        self.strategy = strategy

    def next_code(self, round=0):
        if len(self.history) != 0:
            self.possible_codes.update(self.history[-1])
        self.tree = MCTSTree(self.code, self.possible_codes)
        self.tree.build_tree()
        self.code = self.tree.get_best_move(self.strategy)
        return self.code
