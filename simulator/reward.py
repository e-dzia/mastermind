import enum


class Reward(enum.Enum):
    WIN = 1000
    SAME_COLOR = 5
    SAME_COLOR_AND_SPOT = 10
    USED_TRIES = 100
    NOTHING = 0
