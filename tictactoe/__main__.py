from tictactoe.cli import CLI
from tictactoe.game import Game


def main() -> None:
    cli = CLI()
    _ = Game(cli)
    cli.begin_game()
    cli.end_game()


if __name__ == "__main__":
    main()
