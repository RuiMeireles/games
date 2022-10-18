from dataclasses import dataclass, field
from random import randint
from typing import Dict, List, Optional, Protocol, Set, Tuple

from tictactoe.board import Board
from tictactoe.common import Position, Symbol


@dataclass
class PositionEval:
    score: float
    symbol: Symbol
    next_moves: Set[Position]


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
class RecursiveStrategy:
    eval_table: Dict[Tuple[str, Symbol], PositionEval] = field(default_factory=dict)

    @staticmethod
    def _is_new_score_better(old_score: float, new_score: float, symbol: Symbol) -> bool:
        if symbol not in [Symbol.X, Symbol.O]:
            raise ValueError("Unsupported symbol")
        if symbol == Symbol.X:
            return new_score > old_score
        return new_score < old_score

    def eval_position(self, board: Board, symbol: Symbol) -> float:
        if symbol not in [Symbol.X, Symbol.O]:
            raise ValueError("Unsupported symbol")
        win_score = 1.0 if symbol == Symbol.X else -1.0
        str_board = str(board)
        key = (str_board, symbol)
        # Bail out if this position was already calculated (memoization)
        if key in self.eval_table:
            return self.eval_table[key].score
        # Start evaluation
        winning_moves, forced_moves, other_moves = classify_moves(board, symbol)
        if winning_moves:
            # Wins
            self.eval_table[key] = PositionEval(win_score, symbol, set(winning_moves))
            return win_score
        if forced_moves:
            if len(forced_moves) > 1:
                # Loses
                self.eval_table[key] = PositionEval(-win_score, symbol, set(forced_moves))
                return -win_score
        remaining_moves = forced_moves or other_moves
        # There are no more moves
        if not remaining_moves:
            return 0.0
        # There are more moves, outcome isn't determined yet
        for position in remaining_moves:
            new_board = Board.from_str(str_board)
            new_board.place(position, symbol)
            # Recursive search
            score = self.eval_position(new_board, reverse_symbol(symbol))
            if key not in self.eval_table or self._is_new_score_better(self.eval_table[key].score, score, symbol):
                # Found the first move, or a move better than the current ones
                self.eval_table[key] = PositionEval(score, symbol, set([position]))
                continue
            if self.eval_table[key].score == score:
                self.eval_table[key].next_moves.add(position)
        # Return the best score of all the evaluated moves
        return self.eval_table[key].score
