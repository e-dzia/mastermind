from simulator.game_code import Code
from simulator.color import Color
from players.player import Player


class UserPlayer(Player):
    def next_code(self, round=0):
        value = ""
        for color in list(Color):
            color_str = str(color).replace('Color.', '')
            print(f"                    {color_str} = {color.value}")
        code = Code()
        code.set_from_string("")
        while len(code.colors) != 4:
            value = input("Choose 4 colours for this round: ")
            code.set_from_string(value)
        self.code = code
        return self.code
