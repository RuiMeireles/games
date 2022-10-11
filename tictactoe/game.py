from dataclasses import dataclass
from tictactoe.board import Board
from tictactoe.scoreboard import Scoreboard
from tictactoe.ui import UI


@dataclass
class Game:
    ui: UI
    scoreboard: Scoreboard = Scoreboard()
    board: Board = Board()
