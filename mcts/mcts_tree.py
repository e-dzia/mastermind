import copy
import random

from anytree import AnyNode, RenderTree

from mcts.mcts_node import MCTSNode
from mcts.mcts_player import MCTSStrategy
from players.possible_codes import PossibleCodes
from simulator.game_code import Code


class MCTSTree:
    def __init__(self, code: Code, possible_codes: PossibleCodes,
                 max_round_length=10):
        self.starting_code = code
        self.root = AnyNode(code=self.starting_code)
        self.possible_codes = copy.copy(possible_codes)
        self.max_round_length = max_round_length

    def build_tree(self, num_simulations=5000):
        # first, for every possible next code, we perform one simulation
        for possible_code in self.possible_codes.get_all():
            # print(len(self.possible_codes))
            node = MCTSNode(code=possible_code, parent=self.root)
            node.perform_simulation(self.possible_codes,
                                    next_code=Code(*possible_code))

        # then, we perform a simulation for remaining number of tries
        # nodes to perform simulations are chosen by roulette wheel selection
        num_simulations -= len(self.possible_codes)
        for i in range(num_simulations):
            node = self._get_best_node()
            node.perform_simulation(self.possible_codes,
                                    next_code=Code(*node.code))

    def _get_best_node(self):
        #  Roulette Wheel Selection - probability of choosing every code
        #  is proportional to their mean reward
        sum_points = sum([node.results/node.games_performed
                          for node in self.root.children])
        hit = random.randint(0, int(sum_points) - 1)
        current_sum = 0
        best_node = None
        for node in self.root.children:
            current_sum += node.results/node.games_performed
            if current_sum >= hit:
                best_node = node
                break
        return best_node

    def get_best_move(self, strategy: MCTSStrategy):
        if strategy == MCTSStrategy.GAMES_PERFORMED:
            return self.get_best_move_by_games_performed()
        elif strategy == MCTSStrategy.MEAN_REWARD:
            return self.get_best_move_by_mean_reward()
        else:
            return self.get_best_move_by_games_performed()

    def get_best_move_by_games_performed(self):
        # get code which was simulated the most
        max_games = 0
        best_node = None
        for node in self.root.children:
            if node.games_performed > max_games:
                max_games = node.games_performed
                best_node = node
        return Code(*best_node.code)

    def get_best_move_by_mean_reward(self):
        # get code which has the best mean reward
        max_mean_reward = 0
        best_node = None
        for node in self.root.children:
            if node.results/node.games_performed > max_mean_reward:
                max_mean_reward = node.results/node.games_performed
                best_node = node
        return Code(*best_node.code)
