from dataclasses import dataclass
from random import randint
from typing import List, Optional, Protocol, Tuple

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


def classify_moves(board: Board, symbol: Symbol) -> Tuple[List[Position], List[Position], List[Position]]:
    moves = board.available_positions()
    winning_moves: List[Position] = []
    forced_moves: List[Position] = []
    other_moves: List[Position] = []
    for move in moves:
        b1 = Board.from_str(str(board))
        b1.place(move, symbol)
        if b1.get_winner() == symbol:
            winning_moves.append(move)
    for move in moves:
        rev_symbol = reverse_symbol(symbol)
        b2 = Board.from_str(str(board))
        b2.place(move, rev_symbol)
        if b2.get_winner() == rev_symbol and move not in winning_moves:
            forced_moves.append(move)
    other_moves = list(set(moves) - set(winning_moves) - set(forced_moves))
    return (winning_moves, forced_moves, other_moves)


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


@dataclass
class PositionEval:
    score: float
    next_moves: List[Position]


# class RecursiveStrategy:
#    def eval_position(self, board: Board):
#        winning_moves, forced_moves, other_moves = moves()