import unittest
from parameterized import parameterized

from simulator.game_code import Code
from simulator.color import Color


class TestCode(unittest.TestCase):

    @parameterized.expand([
        ["different1",
         Code(Color.PURPLE, Color.PURPLE, Color.PINK, Color.PURPLE),
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE), False],
        ["different2",
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE),
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE), False],
        ["same",
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE),
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE), True],
    ])
    def test_equals(self, name, c1: Code, c2: Code, result: bool):
        self.assertEqual(result, c1.equals(c2))
        self.assertEqual(result, c2.equals(c1))

    @parameterized.expand([
        ["completely_different",
         Code(Color.PINK, Color.ORANGE, Color.RED, Color.PINK),
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE), 0],
        ["different1", Code(Color.PURPLE, Color.RED, Color.PINK, Color.PURPLE),
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE), 1],
        ["different2",
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE),
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE), 2],
        ["same", Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE),
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE), 4],
    ])
    def test_count_same_color_and_spot(self, name, c1: Code, c2: Code,
                                       result: int):
        self.assertEqual(result, c1.count_same_color_and_spot(c2))

    @parameterized.expand([
        ["completely_different",
         Code(Color.PINK, Color.ORANGE, Color.RED, Color.PINK),
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE), 0],
        ["different1", Code(Color.PURPLE, Color.ORANGE, Color.PINK, Color.PINK),
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE), 1],
        ["different2",
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE),
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE), 2],
        ["different3",
         Code(Color.WHITE, Color.PINK, Color.WHITE, Color.PURPLE),
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE), 1],
        ["same", Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE),
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE), 0],
        ["difficult",
         Code(Color.WHITE, Color.WHITE, Color.YELLOW, Color.YELLOW),
         Code(Color.YELLOW, Color.YELLOW, Color.WHITE, Color.WHITE), 4],
        ["difficult2",
         Code(Color.YELLOW, Color.YELLOW, Color.WHITE, Color.WHITE),
         Code(Color.WHITE, Color.WHITE, Color.YELLOW, Color.YELLOW), 4],
        ["difficult3",
         Code(Color.YELLOW, Color.WHITE, Color.WHITE, Color.YELLOW),
         Code(Color.WHITE, Color.YELLOW, Color.PURPLE, Color.WHITE), 3],
        ["difficult3",
         Code(Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE),
         Code(Color.WHITE, Color.WHITE, Color.YELLOW, Color.YELLOW), 0],
    ])
    def test_count_same_color(self, name, c1: Code, c2: Code, result: int):
        self.assertEqual(result, c1.count_same_color(c2))

    @parameterized.expand([
        ["completely_different",
         Code(Color.PINK, Color.ORANGE, Color.RED, Color.PINK),
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE), 0],
        ["different1", Code(Color.PURPLE, Color.ORANGE, Color.PINK, Color.PINK),
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE), 5],
        ["different2",
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE),
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE), 30],
        ["same", Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE),
         Code(Color.PURPLE, Color.WHITE, Color.YELLOW, Color.PURPLE), 1000],
    ])
    def test_evaluate(self, name, c1: Code, c2: Code, result: int):
        self.assertEqual(result, c1.evaluate(c2, 0))

    @parameterized.expand([
        ["false", Code(Color.PURPLE, Color.ORANGE, Color.PINK, Color.PINK),
         Color.WHITE, False],
        ["true",
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE),
         Color.WHITE, True],
    ])
    def test_contains(self, name, c1: Code, color: Color, result: bool):
        self.assertEqual(result, c1.contains(color))

    @parameterized.expand([
        ["false", Code(Color.PURPLE, Color.ORANGE, Color.PINK, Color.PINK),
         Color.WHITE, 0, False],
        ["true",
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE),
         Color.WHITE, 0, True],
        ["false",
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE),
         Color.WHITE, 1, False],
        ["true",
         Code(Color.WHITE, Color.PURPLE, Color.YELLOW, Color.PURPLE),
         Color.PURPLE, 3, True],
    ])
    def test_contains_in_spot(self, name, c1: Code, color: Color, spot: int,
                              result: bool):
        self.assertEqual(result, c1.contains_in_spot(color, spot))
