import datetime
import os

from players.user_player import UserPlayer
import logging


def main_user():
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

    player = UserPlayer()
    player.play_game()


if __name__ == "__main__":
    start = datetime.datetime.now()

    main_user()

    end = datetime.datetime.now()
    print(f"Time: {end - start}")
