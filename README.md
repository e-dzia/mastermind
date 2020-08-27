# Mastermind

## Simulator

A simulator of the Mastermind game - [Wiki(https://en.wikipedia.org/wiki/Mastermind_(board_game))]

To run the simulator, run `scripts > play_game.py`

## Players

- UserPlayer - anyone can play and try to win
- RandomPlayer - totally random, almost never wins
- SmartPlayer - Smart player works by removing codes that are not possible given current feedback


## Results

### Smart Player

Smart Player has three strategies of choosing next move (after removing codes that are not possible):
- FIRST
- LAST
- RANDOM

Although they are not very different in concept, they have different outcomes. Strategies FIRST and LAST are deterministic, so they were tested just once for every possible game code. RANDOM strategy was tested 10 times for every possible game code. Below you can see the outcomes of these strategies:

| Strategy | max | mean     |
|----------|-----|----------|
| FIRST    | 8.0 | 5.021605 |
| LAST     | 8.0 | 4.934414 |
| RANDOM   | 7.0 | 4.639506 |

As you can see, the RANDOM strategy was the best with the mean of 4.64 rounds to win the game.

