from dataclasses import dataclass, field

from tictactoe.common import GRID_SIZE, Grid, Position, Symbol


def empty_grid() -> Grid:
    return {Position(line, col): Symbol.EMPTY for line in range(GRID_SIZE) for col in range(GRID_SIZE)}


@dataclass
class Board:
    grid: Grid = field(default_factory=empty_grid)

    def place(self, position: Position, symbol: Symbol) -> None:
        if self.grid[position] != Symbol.EMPTY:
            raise ValueError("Can't place a symbol on a non-empty grid cell.")
        self.grid[position] = symbol

    def __str__(self):
        s = ""
        for line in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                s += self.grid[Position(line, col)].value
            s += "\n"
        return s
