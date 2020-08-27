import logging
import pickle
from copy import deepcopy
from datetime import datetime

from anytree import AnyNode, RenderTree

from players.smart_player import SmartPlayer
from simulator.color import Color
from simulator.game_code import Code


def update_player(player, parent_node, code, same_color_and_spot, same_color):
    player.set_results(same_color_and_spot, same_color)

    try:
        if (same_color_and_spot == 4 and
                tuple(code.colors) in player.possible_codes):
            leaf = AnyNode(win=True, num_possibilities=1,
                           same_color_and_spot=same_color_and_spot,
                           same_color=same_color, parent=parent_node,
                           code=code.colors)
        else:
            code = player.next_code(1)
            leaf = None
    except IndexError:
        # leaf = AnyNode(num_possibilities=0,
        #                same_color_and_spot=same_color_and_spot,
        #                same_color=same_color, parent=parent_node)
        leaf = True
        # print(RenderTree(root))
        # a = input("wait")

    return leaf is None


def code_node_depth(player_old, parent_node, code, same_color_and_spot,
                    same_color):
    player = deepcopy(player_old)

    if update_player(player, parent_node, code, same_color_and_spot,
                     same_color):
        node = AnyNode(same_color_and_spot=same_color_and_spot,
                       same_color=same_color,
                       num_possibilites=len(player.possible_codes),
                       parent=parent_node)

        for possible_code in player.possible_codes:
            code = Code(*possible_code)
            player.code = code
            result_node_depth(player, node, code)

    del player


def result_node_depth(player, parent_node, code):
    node = AnyNode(code=code.colors, parent=parent_node)

    if len(player.possible_codes) == 1:
        code_node_depth(player, node, code, 4, 0)
    else:
        for same_color_and_spot in reversed(range(5)):
            for same_color in range(5):
                if same_color_and_spot + same_color <= 4:
                    code_node_depth(player, node, code, same_color_and_spot,
                                    same_color)


if __name__ == "__main__":
    # Note: this takes up so much time and space to count fully
    # that i didn't manage to do it completely but it seems to be
    # working correctly

    start = datetime.now()
    print(start)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    rounds = 50
    colors = list(Color)
    colors.remove(Color.EMPTY)

    player = SmartPlayer()

    root = AnyNode()
    player.code = Code(Color.WHITE, Color.WHITE, Color.YELLOW, Color.YELLOW)

    result_node_depth(player, root, player.code)

    print("end")

    with open('tree.pkl', 'w') as f:
        pickle.dump(root, f)

    # with open('tree.txt', 'w') as f:
    #     f.write(str(RenderTree(root)))

    end = datetime.now()

    print(f"Time: {end-start}")
