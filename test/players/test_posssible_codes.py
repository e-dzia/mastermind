import unittest
from parameterized import parameterized

from players.possible_codes import PossibleCodes
from simulator.game_code import Code
from simulator.color import Color


class TestPossibleCodes(unittest.TestCase):

    def test_init(self):
        codes = PossibleCodes()
        self.assertEqual(6**4, len(codes.possible_codes))

    def test_len(self):
        codes = PossibleCodes()
        self.assertEqual(len(codes.possible_codes), len(codes))

    def test_get(self):
        codes = PossibleCodes()
        self.assertEqual(Code(Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE), codes.get(0))

    @parameterized.expand([
        ["0",
         {'code': Code(Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE),
          'same_color': 0,
          'same_color_and_spot': 3},
         20],
        ["1",
         {'code': Code(Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE),
          'same_color': 0,
          'same_color_and_spot': 2},
         150],
        ["2",
         {'code': Code(Color.WHITE, Color.WHITE, Color.YELLOW, Color.YELLOW),
          'same_color': 0,
          'same_color_and_spot': 4},
         0],
        ["3",
         {'code': Code(Color.WHITE, Color.WHITE, Color.YELLOW, Color.YELLOW),
          'same_color': 4,
          'same_color_and_spot': 0},
         1],
        ["4",
         {'code': Code(Color.WHITE, Color.WHITE, Color.YELLOW, Color.YELLOW),
          'same_color': 2,
          'same_color_and_spot': 0},
         96],
        ["5",
         {'code': Code(Color.WHITE, Color.WHITE, Color.YELLOW, Color.YELLOW),
          'same_color': 0,
          'same_color_and_spot': 0},
         256],
        ["6",
         {'code': Code(Color.PINK, Color.PINK, Color.PINK, Color.PINK),
          'same_color': 0,
          'same_color_and_spot': 0},
         625],
    ])
    def test_update(self, name, history, result):
        codes = PossibleCodes()
        codes.update(history)
        self.assertEqual(result, len(codes))


if __name__ == '__main__':
    unittest.main()
