import unittest

from tictactoe.board import Board
from tictactoe.common import Position, Symbol


class TestBoardMethods(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
