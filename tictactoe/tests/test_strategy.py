import unittest

from tictactoe.board import Board
from tictactoe.common import Position, Symbol
from tictactoe.strategy import classify_moves, random_position, reverse_symbol


class TestStrategyFunctions(unittest.TestCase):
    def test_reverse_symbol(self):
        self.assertEqual(reverse_symbol(Symbol.X), Symbol.O)
        self.assertEqual(reverse_symbol(Symbol.O), Symbol.X)
        with self.assertRaises(KeyError):
            reverse_symbol(Symbol.EMPTY)

    def test_random_position(self):
        positions = [Position(0, 0), Position(row=1, col=1), Position(row=2, col=2)]
        position = random_position(positions)
        self.assertIn(position, positions)

    def test_classify_moves(self):
        str_1 = " OO\n XX\n XO"
        winning_moves, forced_moves, other_moves = classify_moves(Board.from_str(str_1), Symbol.X)
        self.assertEqual(winning_moves, [Position(row=1, col=0)])
        self.assertEqual(forced_moves, [Position(row=0, col=0)])
        self.assertEqual(other_moves, [Position(row=2, col=0)])
        str_2 = "XOO\n X \nX  "
        winning_moves, forced_moves, other_moves = classify_moves(Board.from_str(str_2), Symbol.O)
        self.assertEqual(winning_moves, [])
        self.assertEqual(forced_moves, [Position(row=1, col=0), Position(row=2, col=2)])
        self.assertEqual(other_moves, [Position(row=1, col=2), Position(row=2, col=1)])


# class TestRecursiveStrategy(unittest.TestCase):
