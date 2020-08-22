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

    def evaluate(self, other):
        if self.equals(other):
            return Reward.WIN.value
        return self.count_same_color_and_spot(other) * \
               Reward.SAME_COLOR_AND_SPOT.value + self.count_same_color(other) * \
               Reward.SAME_COLOR.value

    def count_same_color_and_spot(self, other):
        count = 0
        for color1, color2 in zip(self.colors, other.colors):
            if color1 == color2:
                count += 1
        return count

    def count_same_color(self, other):
        count = 0
        for color1, color2 in zip(self.colors, other.colors):
            if color1 != color2:
                same_color = False
                for color_other in other.colors:
                    if color1 == color_other:
                        same_color = True
                if same_color:
                    count += 1
        return count

    def __str__(self):
        return str(self.colors)
