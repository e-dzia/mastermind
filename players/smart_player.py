import logging
import random
import itertools

from players.player import Player
from simulator.game_code import Code
from simulator.color import Color


logger = logging.getLogger(__name__)


class SmartPlayer(Player):
    """Smart player works by removing codes that are not possible given
    current feedback"""

    def __init__(self):
        super().__init__()
        self.possible_codes = []
        colors = list(Color)
        colors.remove(Color.EMPTY)
        self.possible_codes = [p for p in itertools.product(colors, repeat=4)]

    def next_code(self, round=0):
        if round == 0:
            self.code = Code(Color.WHITE, Color.WHITE,
                             Color.YELLOW, Color.YELLOW)
            return self.code
        last_history = self.history[-1]
        self.player_colors = last_history['code'].colors
        self.possible_codes.remove(tuple(self.player_colors))

        if last_history['same_color_and_spot'] > 0:
            self.remove_same_color_and_spot(last_history['same_color_and_spot'])

        if last_history['same_color'] > 0:
            self.remove_same_color(last_history['same_color'])

        self.check_colors_sum(last_history['same_color_and_spot'] +
                              last_history['same_color'])

        if (last_history['same_color'] == 0 and
                last_history['same_color_and_spot'] == 0):
            self.remove_no_colors()

        logger.info(f"Possible codes: {len(self.possible_codes)}")
        return Code(*self.possible_codes[0])

    def remove_no_colors(self):
        for possible_code in self.possible_codes[:]:
            if any(color in possible_code for color in self.player_colors):
                if possible_code in self.possible_codes:
                    self.possible_codes.remove(possible_code)

    def remove_same_color(self, number_of_colors):
        for possible_code in self.possible_codes[:]:
            if sum(1 if color in possible_code else 0
                   for color in self.player_colors) < number_of_colors:
                if possible_code in self.possible_codes:
                    self.possible_codes.remove(possible_code)
            if number_of_colors == 4:
                if (not all(color in self.player_colors
                            for color in possible_code) or
                        not all(color in possible_code
                                for color in self.player_colors)):
                    if possible_code in self.possible_codes:
                        self.possible_codes.remove(possible_code)

                for i, code_position in enumerate(possible_code):
                    if self.player_colors[i] == code_position:
                        if possible_code in self.possible_codes:
                            self.possible_codes.remove(possible_code)

    def remove_same_color_and_spot(self, number_of_colors):
        for possible_code in self.possible_codes[:]:
            remove_code = True
            count = 0
            for i, code_position in enumerate(possible_code):
                if self.player_colors[i] == code_position:
                    count += 1

            if count >= number_of_colors:
                remove_code = False

            if remove_code and possible_code in self.possible_codes:
                self.possible_codes.remove(possible_code)

    def remove_all_good_color(self):
        for possible_code in self.possible_codes[:]:
            if not (all(color in self.player_colors for color in possible_code)
                    and
                    all(color in possible_code
                        for color in self.player_colors)):
                if possible_code in self.possible_codes:
                    self.possible_codes.remove(possible_code)

    def check_colors_sum(self, number_of_colors):
        for possible_code in self.possible_codes[:]:
            if (Code(*possible_code).count_colors_sum(Code(*self.player_colors))
                    != number_of_colors):
                if possible_code in self.possible_codes:
                    self.possible_codes.remove(possible_code)
