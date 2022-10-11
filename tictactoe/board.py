from dataclasses import dataclass, field

from tictactoe.common import GRID_SIZE, Grid, Position, Symbol


def empty_grid() -> Grid:
    return {Position(line, col): Symbol.EMPTY for line in range(GRID_SIZE) for col in range(GRID_SIZE)}


@dataclass
class Board:
    grid: Grid = field(default_factory=empty_grid)

    def from_str(self, s: str):
        rows = s.strip("\n").split("\n")
        if len(rows) != GRID_SIZE:
            raise ValueError("Not a valid string to describe a Board")
        for row, row_str in enumerate(rows):
            if len(row_str) != GRID_SIZE:
                raise ValueError("Not a valid string to describe a Board")
            for col, char in enumerate(row_str):
                self.grid[Position(row, col)] = Symbol._value2member_map_[char]
        return self

    def place(self, position: Position, symbol: Symbol) -> None:
        if self.grid[position] != Symbol.EMPTY:
            raise ValueError("Can't place a symbol on a non-empty grid cell.")
        self.grid[position] = symbol

    def __str__(self):
        s = ""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                s += self.grid[Position(row, col)].value
            s += "\n"
        return s.strip("\n")
