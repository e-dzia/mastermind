from simulator.game import Game
from players.user_player import UserPlayer

print("ready")
game = Game(UserPlayer())
game.play_game()
