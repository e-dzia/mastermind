import unittest
from parameterized import parameterized

from simulator.code import Code
from simulator.color import Color


class TestCode(unittest.TestCase):

    @parameterized.expand([
        ["different1", Code(Color.BLUE, Color.BLUE, Color.GREEN, Color.BLUE), Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE), False],
        ["different2", Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE), Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE), False],
        ["same", Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE), Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE), True],
    ])
    def test_equals(self, name, c1: Code, c2: Code, result: bool):
        self.assertEqual(result, c1.equals(c2))
        self.assertEqual(result, c2.equals(c1))

    @parameterized.expand([
        ["completely_different", Code(Color.GREEN, Color.ORANGE, Color.RED, Color.PINK),
         Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE), 0],
        ["different1", Code(Color.BLUE, Color.BLUE, Color.GREEN, Color.BLUE),
         Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE), 1],
        ["different2",
         Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE),
         Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE), 2],
        ["same", Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE),
         Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE), 4],
    ])
    def test_count_same_color_and_spot(self, name, c1: Code, c2: Code, result: int):
        self.assertEqual(result, c1.count_same_color_and_spot(c2))
        self.assertEqual(result, c2.count_same_color_and_spot(c1))

    @parameterized.expand([
        ["completely_different",
         Code(Color.GREEN, Color.ORANGE, Color.RED, Color.PINK),
         Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE), 0],
        ["different1", Code(Color.BLUE, Color.ORANGE, Color.GREEN, Color.PINK),
         Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE), 1],
        ["different2",
         Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE),
         Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE), 2],
        ["same", Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE),
         Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE), 0],
    ])
    def test_count_same_color(self, name, c1: Code, c2: Code,
                                       result: int):
        self.assertEqual(result, c1.count_same_color(c2))
        self.assertEqual(result, c2.count_same_color(c1))

    @parameterized.expand([
        ["completely_different",
         Code(Color.GREEN, Color.ORANGE, Color.RED, Color.PINK),
         Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE), 0],
        ["different1", Code(Color.BLUE, Color.ORANGE, Color.GREEN, Color.PINK),
         Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE), 5],
        ["different2",
         Code(Color.WHITE, Color.BLUE, Color.YELLOW, Color.PURPLE),
         Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE), 30],
        ["same", Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE),
         Code(Color.BLUE, Color.WHITE, Color.YELLOW, Color.PURPLE), 1000],
    ])
    def test_evaluate(self, name, c1: Code, c2: Code, result: int):
        self.assertEqual(result, c1.evaluate(c2))
        self.assertEqual(result, c2.evaluate(c1))
