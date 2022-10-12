from dataclasses import dataclass, field

from tictactoe.common import GRID_SIZE, Grid, Position, Symbol


def empty_grid() -> Grid:
    return {Position(line, col): Symbol.EMPTY for line in range(GRID_SIZE) for col in range(GRID_SIZE)}


@dataclass
class Board:
    grid: Grid = field(default_factory=empty_grid)

    @classmethod
    def from_str(cls, s: str):
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

    def __str__(self):
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
