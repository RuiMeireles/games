from dataclasses import dataclass, field
from typing import Dict

from tictactoe.common import GRID_SIZE, Grid, Position, Symbol


def empty_grid() -> Grid:
    return {Position(line, col): Symbol.EMPTY for line in range(GRID_SIZE) for col in range(GRID_SIZE)}


@dataclass
class Board:
    grid: Grid = field(default_factory=empty_grid, hash=True)

    @classmethod
    def from_str(cls, s: str) -> "Board":
        str_to_symbol = {symbol.value: symbol for symbol in Symbol}
        error_msg = "Not a valid string to describe a Board"

        board = cls()
        rows = s.strip("\n").split("\n")
        if len(rows) != GRID_SIZE:
            raise ValueError(error_msg)
        for row, row_str in enumerate(rows):
            if len(row_str) != GRID_SIZE:
                raise ValueError(error_msg)
            for col, char in enumerate(row_str):
                try:
                    board.grid[Position(row, col)] = str_to_symbol[char]
                except KeyError:
                    raise ValueError(error_msg)
        return board

    def __str__(self) -> str:
        s = ""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                s += self.grid[Position(row, col)].value
            s += "\n"
        return s.strip("\n")

    def place(self, position: Position, symbol: Symbol) -> None:
        if self.grid[position] != Symbol.EMPTY:
            raise ValueError("Can't place a symbol on a non-empty grid cell.")
        self.grid[position] = symbol

    def _wins_in_rows(self, symbol: Symbol) -> bool:
        for row in range(GRID_SIZE):
            if all([self.grid[Position(row, col)] == symbol for col in range(GRID_SIZE)]):
                return True
        return False

    def _wins_in_cols(self, symbol: Symbol) -> bool:
        for col in range(GRID_SIZE):
            if all([self.grid[Position(row, col)] == symbol for row in range(GRID_SIZE)]):
                return True
        return False

    def _wins_in_diags(self, symbol: Symbol) -> bool:
        if all([self.grid[Position(i, i)] == symbol for i in range(GRID_SIZE)]):
            return True
        if all([self.grid[Position(i, GRID_SIZE - 1 - i)] == symbol for i in range(GRID_SIZE)]):
            return True
        return False

    def get_winner(self) -> Symbol:
        winner: Dict[Symbol, bool] = {}
        for symbol in [Symbol.X, Symbol.O]:
            winner[symbol] = False
            if self._wins_in_rows(symbol) or self._wins_in_cols(symbol) or self._wins_in_diags(symbol):
                winner[symbol] = True
        if all(winner.values()):
            raise ValueError("Invalid Board: More than one winner")
        if winner[Symbol.X]:
            return Symbol.X
        if winner[Symbol.O]:
            return Symbol.O
        return Symbol.EMPTY
