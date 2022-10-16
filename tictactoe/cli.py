from typing import Dict, List


class CLI:
    def begin_game(self) -> None:
        print("\nLet's play Tic Tac Toe.\n")

    def end_game(self) -> None:
        print("\nHope you enjoyed playing.\n")

    def refresh_board(self, board_str: str) -> None:
        row_template = "  {} | {} | {}  \n"
        row_separator = "----+---+----\n"
        rows: List[str] = []
        for row in board_str.strip("\n").split("\n"):
            rows.append(row_template.format(*row))
        print(row_separator.join(rows))

    def get_number_of_players(self) -> int:
        while True:
            text = input("How many humans will play? [0, 1, 2] ")
            if text in ["0", "1", "2"]:
                print()
                return int(text)
            print("Invalid number. Please try again.\n")

    def display_player_names(self, players: List[Dict[str, str]]) -> None:
        """Takes a list of dict with keys ['name', 'value']"""
        for i, player in enumerate(players, 1):
            print(f"Player #{i}: [{player['symbol']}] {player['name']}")
        print()

    def display_positions(self) -> None:
        print("These are the positions you can choose to place your symbol:\n")
        board_str = "123\n456\n789"
        self.refresh_board(board_str)

    def players_turn(self, player_name: str) -> None:
        print(f"It's {player_name} turn.\n")

    def ends_with_win(self, player_name: str) -> None:
        print(f"{player_name} wins.\n")

    def ends_with_draw(self) -> None:
        print("It's a draw.\n")
