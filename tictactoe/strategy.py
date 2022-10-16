from random import randint
from typing import Protocol

from tictactoe.board import Board
from tictactoe.common import Position


class Strategy(Protocol):
    def select_move(self, board: Board) -> Position:
        ...


class RandomStrategy:
    def select_move(self, board: Board) -> Position:
        choices = board.available_positions()
        return choices[randint(0, len(choices) - 1)]
