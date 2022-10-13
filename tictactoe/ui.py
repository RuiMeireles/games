from typing import List, Protocol


class UI(Protocol):
    def begin_game(self) -> None:
        ...

    def end_game(self) -> None:
        ...

    def refresh_board(self, board_str: str) -> None:
        ...

    def get_number_of_players(self) -> int:
        ...

    def display_player_names(self, players: List[str]) -> None:
        ...
