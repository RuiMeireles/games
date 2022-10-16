from typing import Dict, List, Protocol


class UI(Protocol):
    def begin_game(self) -> None:
        ...

    def end_game(self) -> None:
        ...

    def display_board(self, board_str: str) -> None:
        ...

    def get_number_of_human_players(self) -> int:
        ...

    def display_player_names(self, players: List[Dict[str, str]]) -> None:
        """Takes a list of dict with keys ['name', 'value']"""
        ...

    def display_position_numbers(self) -> None:
        ...

    def players_turn(self, player_name: str) -> None:
        ...

    def get_move_from_human(self, available_moves: List[int]) -> int:
        ...

    def ends_with_win(self, player_name: str) -> None:
        ...

    def ends_with_draw(self) -> None:
        ...
