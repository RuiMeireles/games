import unittest

from tictactoe.board import Board
from tictactoe.common import Position, Symbol


class TestBoardBaseMethods(unittest.TestCase):
    def test_new_board_has_empty_grid(self):
        str_empty_board = "   \n   \n   "
        self.assertEqual(str(Board()), str_empty_board)

    def test_new_board_from_str(self):
        str_board = "X  \n   \n   "
        self.assertEqual(str(Board.from_str(str_board)), str_board)

    def test_new_board_from_invalid_str_fails(self):
        with self.assertRaises(ValueError):
            Board.from_str(" X \n O \nX")
        with self.assertRaises(ValueError):
            Board.from_str(" X \n O ")
        with self.assertRaises(ValueError):
            Board.from_str(" R \n O \n X ")

    def test_board_place_symbol_succeeds(self):
        board = Board()
        board.place(Position(1, 1), Symbol.X)
        str_board = "   \n X \n   "
        self.assertEqual(str(board), str_board)

    def test_board_place_symbol_fails(self):
        board = Board.from_str("   \n X \n   ")
        with self.assertRaises(ValueError):
            board.place(Position(1, 1), Symbol.O)


class TestBoardWinner(unittest.TestCase):
    def test_board_wins_in_rows_is_true(self):
        board = Board.from_str(" O \nXXX\n O ")
        self.assertTrue(board._wins_in_rows(Symbol.X))  # type: ignore

    def test_board_wins_in_rows_is_false(self):
        board = Board.from_str(" O \nXXX\n O ")
        self.assertFalse(board._wins_in_rows(Symbol.O))  # type: ignore

    def test_board_wins_in_cols_is_true(self):
        board = Board.from_str(" O \nXOX\n O ")
        self.assertTrue(board._wins_in_cols(Symbol.O))  # type: ignore

    def test_board_wins_in_cols_is_false(self):
        board = Board.from_str(" O \nXOX\n O ")
        self.assertFalse(board._wins_in_cols(Symbol.X))  # type: ignore

    def test_board_wins_in_diags_is_true(self):
        board = Board.from_str(" XO\nXOX\nO X")
        self.assertTrue(board._wins_in_diags(Symbol.O))  # type: ignore

    def test_board_wins_in_diags_is_false(self):
        board = Board.from_str(" XO\nXOX\nO X")
        self.assertFalse(board._wins_in_diags(Symbol.X))  # type: ignore

    def test_get_winner_is_true(self):
        board = Board.from_str(" X \n XO\n XO")
        self.assertEqual(board.get_winner(), Symbol.X)

    def test_get_winner_is_false(self):
        board = Board.from_str(" XX\n OO\n XO")
        self.assertEqual(board.get_winner(), Symbol.EMPTY)

    def test_get_winner_is_invalid(self):
        board = Board.from_str("XXX\nOOO\n XO")
        with self.assertRaises(ValueError):
            board.get_winner()


if __name__ == "__main__":
    unittest.main()
