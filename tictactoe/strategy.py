from random import randint
from typing import List, Optional, Protocol

from tictactoe.board import Board
from tictactoe.common import Position, Symbol


def reverse_symbol(symbol: Symbol) -> Symbol:
    mapping = {
        Symbol.X: Symbol.O,
        Symbol.O: Symbol.X,
    }
    return mapping[symbol]


def random_position(positions: List[Position]) -> Position:
    return positions[randint(0, len(positions) - 1)]


class Strategy(Protocol):
    def select_move(self, board: Board, symbol: Symbol) -> Position:
        ...


class RandomStrategy:
    def select_move(self, board: Board, symbol: Symbol) -> Position:
        return random_position(board.available_positions())


class LookAheadStrategy:
    def _select_move_recursive(self, board: Board, symbol: Symbol) -> Optional[Position]:
        best_choices: List[Position] = []
        second_best_choices: List[Position] = []
        choices = board.available_positions()
        if not choices:
            return None
        for choice in choices:
            b = Board.from_str(str(board))
            b.place(choice, symbol)
            if b.get_winner() == symbol:
                best_choices.append(choice)
        # If it found a winning move
        if best_choices:
            return random_position(best_choices)
        # Look ahead
        for choice in choices:
            b = Board.from_str(str(board))
            b.place(choice, symbol)
            second_best_choice = self._select_move_recursive(b, reverse_symbol(symbol))
            if second_best_choice is not None:
                second_best_choices.append(second_best_choice)
        # If it found a defensive move
        if second_best_choices:
            return random_position(second_best_choices)
        # Nothing great. Play random
        return random_position(choices)

    def select_move(self, board: Board, symbol: Symbol) -> Position:
        move = self._select_move_recursive(board, symbol)
        assert move is not None
        return move
