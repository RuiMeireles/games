from dataclasses import dataclass, field
from typing import List

from tictactoe.board import Board
from tictactoe.common import Symbol
from tictactoe.player import Player, HumanPlayer, CPUPlayer
from tictactoe.scoreboard import Scoreboard
from tictactoe.ui import UI

PLAYER_TYPE = {
    0: (CPUPlayer, CPUPlayer),
    1: (HumanPlayer, CPUPlayer),
    2: (HumanPlayer, HumanPlayer),
}

SYMBOL_TYPE = {
    0: Symbol.X,
    1: Symbol.O,
}


@dataclass
class Game:
    ui: UI
    scoreboard: Scoreboard = field(default_factory=Scoreboard)
    board: Board = field(default_factory=Board)
    num_players: int = field(init=False)
    players: List[Player] = field(default_factory=list, init=False)

    def play(self) -> None:
        self.ui.begin_game()

        self.num_players = self.ui.get_number_of_players()
        for i, player_type in enumerate(PLAYER_TYPE[self.num_players]):
            if player_type == HumanPlayer:
                self.players.append(HumanPlayer(f"Human{i + 1}", SYMBOL_TYPE[i], self.ui))
            else:
                self.players.append(CPUPlayer(f"CPU{i + 1}", SYMBOL_TYPE[i]))

        self.ui.display_player_names([p.name for p in self.players])
        self.ui.refresh_board(str(self.board))
        self.ui.refresh_board(str(Board().from_str("XOX\n XO\n  O")))
        self.ui.end_game()
