from enum import Enum


class MCTSStrategy(Enum):
    GAMES_PERFORMED = 1
    MEAN_REWARD = 2


class SelectionStrategy(Enum):
    ROULETTE_WHEEL = 1
    TOURNAMENT = 2
