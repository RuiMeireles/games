import unittest

from tictactoe.board import Board
from tictactoe.common import Position, Symbol
from tictactoe.strategy import RecursiveStrategy, classify_moves, random_position, reverse_symbol


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
        str_3 = "XOX\nOXO\nXOX"
        winning_moves, forced_moves, other_moves = classify_moves(Board.from_str(str_3), Symbol.O)
        self.assertEqual(winning_moves, [])
        self.assertEqual(forced_moves, [])
        self.assertEqual(other_moves, [])


class TestRecursiveStrategy(unittest.TestCase):
    def test_is_new_score_better_is_True(self):
        r = RecursiveStrategy()
        self.assertTrue(r._is_new_score_better(0.0, 1, Symbol.X))  # type: ignore
        self.assertTrue(r._is_new_score_better(0.0, -1, Symbol.O))  # type: ignore
        self.assertFalse(r._is_new_score_better(0.0, 0.0, Symbol.X))  # type: ignore
        self.assertFalse(r._is_new_score_better(0.0, 1, Symbol.O))  # type: ignore
        with self.assertRaises(ValueError):
            r._is_new_score_better(0.0, -1, Symbol.EMPTY)  # type: ignore

    def test_eval_position(self):
        # Winning positions for X
        r = RecursiveStrategy()
        self.assertEqual(r.eval_position(Board.from_str("XOO\n X \nX  "), Symbol.X), 1.0)
        self.assertEqual(r.eval_position(Board.from_str("XOX\n X \nX  "), Symbol.O), 1.0)
        # Winning for X, all moves are forced
        self.assertEqual(r.eval_position(Board.from_str("X O\n O \n  X"), Symbol.X), 1.0)
        # Winning position for both
        self.assertEqual(r.eval_position(Board.from_str("XO \nXO \n   "), Symbol.O), -1.0)
        self.assertEqual(r.eval_position(Board.from_str("XO \nXO \n   "), Symbol.X), 1.0)
        # Drawing positions for both
        self.assertEqual(r.eval_position(Board.from_str("OXO\n X \n OX"), Symbol.X), 0.0)
        self.assertEqual(r.eval_position(Board.from_str("OXO\n X \n OX"), Symbol.O), 0.0)
        self.assertEqual(r.eval_position(Board.from_str("O  \n X \nX  "), Symbol.O), 0.0)
        self.assertEqual(r.eval_position(Board.from_str("O O\n X \nX  "), Symbol.X), 0.0)
        self.assertEqual(r.eval_position(Board.from_str("XO \n O \n  X"), Symbol.X), 0.0)
        self.assertEqual(r.eval_position(Board.from_str("X  \n O \n  X"), Symbol.O), 0.0)
        # Drawing positions, initial stages
        self.assertEqual(r.eval_position(Board.from_str("   \n X \n   "), Symbol.O), 0.0)
        self.assertEqual(r.eval_position(Board.from_str("X  \n   \n   "), Symbol.O), 0.0)
        self.assertEqual(r.eval_position(Board.from_str("X  \n O \n   "), Symbol.X), 0.0)
        self.assertEqual(r.eval_position(Board.from_str("X  \n O \n  X"), Symbol.O), 0.0)
