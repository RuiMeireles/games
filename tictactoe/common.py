from enum import Enum
from typing import NamedTuple

GRID_SIZE = 3


class Symbol(Enum):
    X = "X"
    O = "O"  # noqa
    EMPTY = " "


class Position(NamedTuple):
    row: int
    col: int


Grid = dict[Position, Symbol]
