from abc import ABC, abstractmethod
from dataclasses import dataclass

from tictactoe.board import Board
from tictactoe.common import Symbol
from tictactoe.strategy import Strategy
from tictactoe.ui import UI


@dataclass
class Player(ABC):
    name: str
    symbol: Symbol

    @abstractmethod
    def play_move(self, board: Board) -> None:
        raise NotImplementedError


@dataclass
class HumanPlayer(Player):
    ui: UI

    def play_move(self, board: Board) -> None:
        available_moves = [board.position_to_index(pos) for pos in board.available_positions()]
        index = self.ui.get_move_from_human(available_moves)
        position = board.index_to_position(index)
        board.place(position, self.symbol)


@dataclass
class CPUPlayer(Player):
    strategy: Strategy

    def play_move(self, board: Board) -> None:
        position = self.strategy.select_move(board)
        board.place(position, self.symbol)
