import unittest

from tictactoe.board import Board


class TestBoardMethods(unittest.TestCase):
    def test_new_board_has_empty_grid(self):
        self.assertEqual(str(Board()), "   \n   \n   ")

    def test_new_board_from_str(self):
        self.assertEqual(str(Board().from_str("X  \n   \n   ")), "X  \n   \n   ")


if __name__ == "__main__":
    unittest.main()
