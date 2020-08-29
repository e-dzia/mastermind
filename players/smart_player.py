import logging
import itertools
import random
from enum import Enum

from players.enums import SmartStrategy
from players.player import Player
from players.possible_codes import PossibleCodes
from simulator.game_code import Code
from simulator.color import Color


logger = logging.getLogger(__name__)


class SmartPlayer(Player):
    """Smart player works by removing codes that are not possible given
    current feedback"""

    def __init__(self, strategy: SmartStrategy = SmartStrategy.FIRST):
        super().__init__()
        self.possible_codes = PossibleCodes()
        self.player_colors = self.code.colors
        self.strategy = strategy

    def reset(self):
        self.__init__(self.strategy)

    def next_code(self, round=0):
        if len(self.history) == 0:
            self.code = Code(Color.WHITE, Color.WHITE,
                             Color.YELLOW, Color.YELLOW)
            return self.code

        self.possible_codes.update(self.history[-1])

        self.code = self.possible_codes.get(0)
        if self.strategy == SmartStrategy.RANDOM:
            self.code = self.possible_codes.get_random()
        elif self.strategy == SmartStrategy.LAST:
            self.code = self.possible_codes.get(len(self.possible_codes) - 1)

        return self.code
