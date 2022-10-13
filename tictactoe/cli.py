from typing import List


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

    def display_player_names(self, players: List[str]) -> None:
        for i, player in enumerate(players, 1):
            print(f"Player #{i}: {player}")
        print()
