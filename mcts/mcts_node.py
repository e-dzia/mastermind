import copy

from anytree import AnyNode

from players.possible_codes import PossibleCodes
from simulator.game_code import Code
from simulator.reward import Reward


class MCTSNode():
    def __init__(self, code: Code):
        self.games_performed = 0
        self.results = 0
        self.code = code

    def perform_simulation(self, possible_codes_old: PossibleCodes,
                           next_code: Code=None, max_round_length=10):
        possible_codes = copy.copy(possible_codes_old)
        if len(possible_codes) == 0:
            return 0
        if next_code is None:
            next_code = possible_codes.get_random()
        i = 0
        for i in range(max_round_length):
            fake_code = possible_codes.get_random()
            same_color, same_color_and_spot = fake_code.compare(next_code)
            possible_codes.update({'code': next_code,
                                   'same_color': same_color,
                                   'same_color_and_spot': same_color_and_spot})
            if len(possible_codes) <= 1:
                break
            next_code = possible_codes.get_random()
        self.games_performed += 1
        self.results += Reward.WIN.value - Reward.USED_TRIES.value * (i+1)
        return i

    def __repr__(self):
        return f"{self.code}, {self.games_performed}, {self.results}"
