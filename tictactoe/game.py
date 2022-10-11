from dataclasses import dataclass

from tictactoe.board import Board
from tictactoe.scoreboard import Scoreboard
from tictactoe.ui import UI


@dataclass
class Game:
    ui: UI
    scoreboard: Scoreboard = Scoreboard()
    board: Board = Board()

    def play(self) -> None:
        self.ui.begin_game()
        self.ui.refresh_board(str(self.board))
        self.ui.refresh_board(str(Board().from_str("XOX\n XO\n  O")))
        self.ui.end_game()
