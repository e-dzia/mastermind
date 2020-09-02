import itertools
import logging
import random

from simulator.color import Color
from simulator.game_code import Code

logger = logging.getLogger(__name__)


class PossibleCodes:
    def __init__(self):
        self.possible_codes = []
        colors = list(Color)
        colors.remove(Color.EMPTY)
        self.possible_codes = [p for p in itertools.product(colors, repeat=4)]
        self.possible_codes = [Code(*code) for code in self.possible_codes]
        self.code = None

    def get(self, index):
        return self.possible_codes[index]

    def __len__(self):
        return len(self.possible_codes)

    def get_random(self):
        return random.choice(self.possible_codes)

    def get_all(self):
        return self.possible_codes

    def update(self, last_history):
        self.code = last_history['code']
        self.possible_codes = [code for code in self.possible_codes
                               if code != self.code]

        self._update_by_received_stats(last_history['same_color'],
                                       last_history['same_color_and_spot'])

        # logger.info(f"Possible codes: {len(self.possible_codes)}")

    def _update_by_received_stats(self, same_color, same_color_and_spot):
        self._remove_same_color_and_spot(same_color_and_spot)
        self._remove_same_color(same_color)

    def _remove_same_color(self, number_of_colors):
        self.possible_codes = [
            possible_code for possible_code in self.possible_codes
            if possible_code.count_same_color(self.code)
               == number_of_colors]

    def _remove_same_color_and_spot(self, number_of_colors):
        self.possible_codes = [
            possible_code for possible_code in self.possible_codes
            if possible_code.count_same_color_and_spot(self.code)
               == number_of_colors]

    def _remove_code(self, code_to_remove):
        if code_to_remove in self.possible_codes:
            self.possible_codes.remove(code_to_remove)
