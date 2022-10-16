from dataclasses import dataclass, field
from typing import List

from tictactoe.board import Board
from tictactoe.common import Symbol
from tictactoe.player import Player, HumanPlayer, CPUPlayer
from tictactoe.scoreboard import Scoreboard
from tictactoe.ui import UI

PLAYER_COMBINATIONS = {
    0: (CPUPlayer, CPUPlayer),
    1: (HumanPlayer, CPUPlayer),
    2: (HumanPlayer, HumanPlayer),
}

SYMBOL_INDEX = {
    0: Symbol.X,
    1: Symbol.O,
}


def do_turn(ui: UI, board: Board, player: Player) -> bool:
    """Returns True if the player wins"""
    ui.players_turn(player.name)
    player.play_move(board)
    ui.display_board(str(board))
    return False


@dataclass
class Game:
    ui: UI
    scoreboard: Scoreboard = field(default_factory=Scoreboard)
    board: Board = field(default_factory=Board)
    num_human_players: int = field(init=False)
    players: List[Player] = field(default_factory=list, init=False)
    player1_starts: bool = field(default=True, init=False)

    def play(self) -> None:
        self.ui.begin_game()

        # Get the number of human players
        self.num_human_players = self.ui.get_number_of_human_players()
        for i, player_type in enumerate(PLAYER_COMBINATIONS[self.num_human_players]):
            if player_type == HumanPlayer:
                self.players.append(HumanPlayer(f"Human{i + 1}", SYMBOL_INDEX[i], self.ui))
            else:
                self.players.append(CPUPlayer(f"CPU{i + 1}", SYMBOL_INDEX[i]))
        self.ui.display_player_names([{"name": p.name, "symbol": p.symbol.value} for p in self.players])
        self.ui.display_position_numbers()

        # Play by turns
        index = 0 if self.player1_starts else 1
        while True:
            player = self.players[index]
            win = do_turn(self.ui, self.board, player)
            if win:
                self.ui.ends_with_win(player.name)
                break
            if not self.board.available_positions():
                self.ui.ends_with_draw()
                break
            index = (index + 1) % 2

        # self.ui.display_board(str(self.board))
        # self.ui.display_board(str(Board().from_str("XOX\n XO\n  O")))
        self.ui.end_game()
