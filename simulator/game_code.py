from simulator.color import Color
from simulator.reward import Reward


class Code:
    colors = [Color.EMPTY, Color.EMPTY, Color.EMPTY, Color.EMPTY]

    def __init__(self, color1: Color = Color.EMPTY, color2: Color = Color.EMPTY,
                 color3: Color = Color.EMPTY, color4: Color = Color.EMPTY):
        self.colors = [color1, color2, color3, color4]

    def equals(self, other):
        if self.colors.__eq__(other.colors):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.equals(other)

    def contains(self, color: Color):
        return color in self.colors

    def contains_in_spot(self, color: Color, spot: int):
        return color == self.colors[spot]

    def evaluate(self, other, used_tries):
        if self.equals(other):
            return Reward.WIN.value - used_tries * Reward.USED_TRIES.value
        return (self.count_same_color_and_spot(other) *
                Reward.SAME_COLOR_AND_SPOT.value +
                self.count_same_color(other) * Reward.SAME_COLOR.value
                - used_tries * Reward.USED_TRIES.value)

    def count_same_color_and_spot(self, other):
        return sum([color1 == color2
                    for color1, color2 in zip(self.colors, other.colors)])

    def count_same_color(self, other):
        used_positions = [i if color1 == color2 else None
                          for i, (color1, color2) in
                          enumerate(zip(self.colors, other.colors))]
        return sum([color1 != color2 and
                    self._has_same_color(other, color1, used_positions)
                    for color1, color2 in zip(self.colors, other.colors)])

    @staticmethod
    def _has_same_color(other, color1, used_positions):
        same_color = False
        for i, color_other in enumerate(other.colors):
            if color1 == color_other and i not in used_positions:
                same_color = True
                used_positions.append(i)
                break
        return same_color

    def __str__(self):
        return str(self.colors)
