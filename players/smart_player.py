import logging
import itertools
import random
from enum import Enum

from players.player import Player
from simulator.game_code import Code
from simulator.color import Color


logger = logging.getLogger(__name__)


class Strategy(Enum):
    RANDOM = 0
    FIRST = 1
    LAST = 2
    BEST = 3


class SmartPlayer(Player):
    """Smart player works by removing codes that are not possible given
    current feedback"""

    def __init__(self, strategy: Strategy = Strategy.FIRST):
        super().__init__()
        self.possible_codes = []
        colors = list(Color)
        colors.remove(Color.EMPTY)
        self.possible_codes = [p for p in itertools.product(colors, repeat=4)]
        self.player_colors = self.code.colors
        self.strategy = strategy

    def next_code(self, round=0):
        if len(self.history) == 0:
            self.code = Code(Color.WHITE, Color.WHITE,
                             Color.YELLOW, Color.YELLOW)
            return self.code

        last_history = self.history[-1]
        self.player_colors = last_history['code'].colors
        self.possible_codes.remove(tuple(self.player_colors))

        self._update_by_received_stats(last_history['same_color'],
                                       last_history['same_color_and_spot'])

        logger.info(f"Possible codes: {len(self.possible_codes)}")

        self.code = Code(*self.possible_codes[0])
        if self.strategy == Strategy.RANDOM:
            self.code = Code(*random.choice(self.possible_codes))
        elif self.strategy == Strategy.LAST:
            self.code = Code(*self.possible_codes[len(self.possible_codes) - 1])

        return self.code

    def _update_by_received_stats(self, same_color, same_color_and_spot):
        self._remove_same_color_and_spot(same_color_and_spot)
        self._remove_same_color(same_color)

    def _remove_same_color(self, number_of_colors):
        for possible_code in self.possible_codes[:]:
            if (Code(*possible_code).count_same_color(self.code)
                    != number_of_colors):
                self._remove_code(possible_code)

    def _remove_same_color_and_spot(self, number_of_colors):
        for possible_code in self.possible_codes[:]:
            if (Code(*possible_code).count_same_color_and_spot(self.code)
                    != number_of_colors):
                self._remove_code(possible_code)

    def _remove_code(self, code_to_remove):
        if code_to_remove in self.possible_codes:
            self.possible_codes.remove(code_to_remove)
