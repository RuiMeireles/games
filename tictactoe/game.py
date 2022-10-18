from dataclasses import dataclass, field
from functools import partial
from typing import List, Optional

from tictactoe.board import Board
from tictactoe.common import Symbol
from tictactoe.player import Player, HumanPlayer, CPUPlayer
from tictactoe.scoreboard import Scoreboard
from tictactoe.strategy import RecursiveStrategy, Strategy
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
    if board.get_winner() != Symbol.EMPTY:
        raise ValueError("The game is already over, can't play an additional turn.")
    ui.players_turn(player.name)
    player.play_move(board)
    ui.display_board(str(board))
    if board.get_winner() == player.symbol:
        return True
    return False


RecursiveStrategy5 = partial(RecursiveStrategy, max_depth=5)


@dataclass
class Game:
    ui: UI
    board: Board = field(default_factory=Board)
    strategy_cpu1: Strategy = field(default_factory=RecursiveStrategy)
    strategy_cpu2: Strategy = field(default_factory=RecursiveStrategy5)
    num_human_players: Optional[int] = field(default=None)
    scoreboard: Scoreboard = field(default_factory=Scoreboard)
    player1_starts: bool = field(default=True)

    def play(self) -> None:
        players: List[Player] = []
        strategies = [self.strategy_cpu1, self.strategy_cpu2]

        self.ui.begin_game()

        # Instanciate players
        if self.num_human_players is None:
            self.num_human_players = self.ui.get_number_of_human_players()
        for i, player_type in enumerate(PLAYER_COMBINATIONS[self.num_human_players]):
            if player_type == HumanPlayer:
                players.append(HumanPlayer(f"Human{i + 1}", SYMBOL_INDEX[i], ui=self.ui))
            else:
                players.append(CPUPlayer(f"CPU{i + 1}", SYMBOL_INDEX[i], strategy=strategies.pop(0)))
        self.ui.display_player_names([{"name": p.name, "symbol": p.symbol.value} for p in players])
        if self.num_human_players > 0:
            self.ui.display_position_numbers()

        # Play by turns
        index = 0 if self.player1_starts else 1
        while True:
            player = players[index]
            win = do_turn(self.ui, self.board, player)
            if win:
                self.ui.ends_with_win(player.name)
                break
            if not self.board.available_positions():
                self.ui.ends_with_draw()
                break
            index = (index + 1) % 2

        # End
        self.ui.end_game()
