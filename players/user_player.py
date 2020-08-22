from simulator.game_code import Code
from simulator.color import Color
from players.player import Player


class UserPlayer(Player):
    def next_code(self, round=0):
        print("""                    WHITE = 0
                    YELLOW = 1
                    ORANGE = 2
                    RED = 3
                    PINK = 4
                    PURPLE = 5
                    BLUE = 6
                    GREEN = 7""")
        value = ""
        while len(value) != 4:
            value = input("Choose 4 colours for this round: ")
        code_list = []
        for spot in value:
            code_list.append(Color(int(spot)))
        code = Code(*code_list)
        self.code = code
        return self.code
