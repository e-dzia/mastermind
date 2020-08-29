# Mastermind

## Simulator

A simulator of the [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game) game.

To run the simulator, run `scripts > play_game.py`

## Players

- UserPlayer - anyone can play and try to win
- RandomPlayer - totally random, almost never wins
- SmartPlayer - Smart player works by removing codes that are not possible given current feedback
- MCTSPlayer - Player using Monte Carlo Tree Search (or rather a strategy based on MCTS)


## Results

### Smart Player

Smart Player removes all codes that are not possible given current feedback. He doesn't do anything more. Smart Player has three strategies of choosing next move (after removing codes that are not possible):
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

### MCTS Player

MCTS Player is non-deterministic, but its playouts take much more time than Smart Player's (~30 sec when choosing first codes, ~6 sec whith pre-calculated first codes (see below)) so I performed only one simulation per possible code and it took about ~1h45min to compute.

#### Pre-calculated first codes

To reduce time, I also performed pre-calculation of the first code to choose (because it took really long time) and chose 10 best codes of 100 000 simulations for both strategies (20 codes total). The algorithms chooses randomly from them to get the first code. Then standard MCTS algorithm is performed.

#### Results

MCTS Player has two strategies to choose the next move:
- GAMES_PERFORMED - it takes only the number of performed simulations
- MEAN_REWARD - it takes the sum of obtained rewards and divides it by the number of performed simulations

Player chooses a move (code) with the highest value of the corresponding metric.


| Strategy         | max  | mean     |
|------------------|------|----------|
| GAMES_PERFORMED  | 7    | 4.492283 |
| MEAN_REWARD      | 6    | 4.407407 |

Sd you can see, the results are significantly better than from a previous method (Smart Player).

#### How MCTS works?

[MCTS](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) is a heuristic search algorithm. It is based on the idea of simulations. 

Before choosing a next move (in this case - next code) the player performs multiple simulations of possible outcomes of the game for every possible move. After the first simulations, he uses more frequently the moves with better outcomes. He also simulates the moves of his opponent and of course the opponent chooses moves that are best for him (as in minimax strategy). When he exceeds a given number of simulations (or time), he chooses a move with the biggest number of simulations.

In Mastermind the opponent cannot really choose his moves, so I decided to simplify this method and perform simulations only for possible codes at the moment. This means I didn't build the whole tree - just one level. (I don't even know if I can still call it 'MCTS', but I was really inspired by this method. Maybe just 'Monte Carlo' would be better.) 

