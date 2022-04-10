# Mastermind

## Simulator

A simulator of the [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) game.

To run the simulator, run `scripts/play_game.py`.

To watch a single game played by one of the players, run `scripts/watch_game.py`.

## Players

- UserPlayer - anyone can play and try to win
- RandomPlayer - totally random, almost never wins
- SmartPlayer - Smart player works by removing codes that are not possible 
given current feedback
- MCTSPlayer - Player using Monte Carlo Tree Search (or rather a strategy 
based on MCTS)


## Results

### State of the art

Donald Knuth [1] proposed a minimax method that requires 4.478 guesses on 
average to find the code with a maximum of 5 guesses.

**State-of-the-art** result is a depth-first search which Kenji Koyama and 
Tony W. Lai performed [2] - showing that the optimal method for solving a 
random code could achieve an average of 5625/1296 = 4.3403 (and a maximum 
of 6 guesses).

### Smart Player

```python
main_experiments(player=SmartPlayer(Strategy.FIRST))
```
from `scripts/experiments.py`

Smart Player removes all codes that are not possible given current feedback. 
He doesn't do anything more. Smart Player has three strategies of 
choosing next move (after removing codes that are not possible):
- FIRST
- LAST
- RANDOM

Although they are not very different in concept, they have different outcomes.
 Strategies FIRST and LAST are deterministic, so they were tested just once
  for every possible game code. RANDOM strategy was tested 50 times for 
  every possible game code. Below you can see the outcomes of these strategies:

| Strategy | max | mean     |
|----------|-----|----------|
| FIRST    | 8.0 | 5.021605 |
| LAST     | 8.0 | 4.934414 |
| RANDOM   | 8.0 | 4.632022 |

As you can see, the RANDOM strategy was the best with the mean of 4.63 rounds 
to win the game.

### MCTS Player

```python
main_experiments(player=MCTSPlayer(MCTSStrategy.MEAN_REWARD))
```
from `scripts/experiments.py`

MCTS Player is non-deterministic, but its playouts take much more time than 
Smart Player's (~30 sec when choosing first codes, ~6 sec whith pre-calculated 
first codes (see below)) so I performed only 10 simulations per possible code.

#### Pre-calculated first codes

To reduce time, I also performed pre-calculation of the first code to choose 
(because it took really long time) and chose 10 best codes of 100 000 
simulations for both strategies (20 codes total). The algorithms chooses 
randomly from them to get the first code. Then standard MCTS algorithm
is performed.

#### Results

MCTS Player has two strategies to choose the next move:
- GAMES_PERFORMED - it takes only the number of performed simulations 
(as in original MCTS strategy)
- MEAN_REWARD - it takes the sum of obtained rewards and divides it by 
the number of performed simulations

Player chooses a move (code) with the highest value of the corresponding metric.

**Num simulations** is the number of simulations performed in each round. 
Of course even more simulations means more time to compute everything 
(~10 sec per game), but it *might* produce better results (in my experiments 
it didn't though).


| Strategy        | Num simulations | max | mean     |
|-----------------|-----------------|-----|----------|
| GAMES_PERFORMED | 10              | 9   | 4.885416 |
|                 | 5 000           | 7   | 4.532484 |
|                 | 10 000          | 7   | 4.507948 |
| MEAN_REWARD     | 10              | 8   | 4.588888 |
|                 | 5 000           | 7   | 4.442747 |
|                 | 10 000          | 7   | 4.436420 |

 (10 simulations for each code)

As you can see, the results are significantly better than from a previous method
 (Smart Player) - mean of 4.44 to win the game.

I also tried the version of this algorithm where the player can use any code 
(not only possible ones), but it was significantly worse and it took much more 
time to compute, so I abandoned this version. 

This method can be improved, possible improvements:
- Other method of choosing nodes to run simulations on (currently it's roulette 
wheel selection)
- Other method of choosing next move (other than MEAN_REWARD and GAMES_PERFORMED)
- Other number of simulations

#### Results - tournament selection

Tournament selection is the type of node selection where at first step 
`k` nodes are chosen randomly and then the best one is selected.

| Strategy        | Num simulations | max | mean     |
|-----------------|-----------------|-----|----------|
| GAMES_PERFORMED | 10              | 9   | 4.844444 |
|                 | 5 000           | x   | x |
|                 | 10 000          | x   | x |
| MEAN_REWARD     | 10              | 7   | 4.576929 |
|                 | 5 000           | x   | x |
|                 | 10 000          | x   | x |

As far, the results are alike for the mean_reward strategy, but far worse for 
games_performed strategy.

#### How MCTS works?

[MCTS](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) is a heuristic 
search algorithm. It is based on the idea of simulations. 

Before choosing a next move (in this case - a next code) the player performs 
multiple simulations of possible outcomes of the game for every possible move. 
After the first simulations, he uses more frequently the moves with better 
outcomes. He also simulates the moves of his opponent and of course the 
opponent chooses moves that are best for him (as in the minimax strategy). 
When he exceeds a given number of simulations (or time), he chooses a move 
with the biggest number of simulations.

In Mastermind the opponent cannot really choose his moves, so I decided to 
simplify this method and perform simulations only for possible codes at the 
moment. This means I didn't build the whole tree - just one level. 
(I don't even know if I can still call it 'MCTS', but I was really inspired 
by this method. Maybe just 'Monte Carlo' would be better.) 

# How to run the code

1. Install all requirements from `requirements.txt`.

2. Add `project` to the PYTHONPATH, e.g. `export PYTHONPATH=~/mastermind/project`

3. Run the script, e.g. `project/scripts/play_game.py`.

4. To run the tests (inside the `project` directory): `python -m unittest discover test`


# References

[1] Knuth, Donald (1976–77). "The Computer as Master Mind" ([PDF](http://www.cs.uni.edu/~wallingf/teaching/cs3530/resources/knuth-mastermind.pdf)). J. Recr. Math. (9): 1–6.

[2] Kenji Koyama and Tony W. Lai. An optimal Mastermind Strategy. Journal of Recreational Mathematics, 25(4):251–256, 1993.

[3] Geoffroy Ville. An Optimal Mastermind (4,7) Strategy and More Results in the Expected Case. ([PDF](https://arxiv.org/pdf/1305.1010.pdf)) 2013

[4] Wei-Fu Lu, Ji-Kai Yang, Hsueh-Ting Chu. Playing Mastermind Game by using Reinforcement Learning ([PDF](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNxFsmGq/pdf)). 2017 First IEEE International Conference on Robotic Computing, 2017.