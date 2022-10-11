from tictactoe.cli import CLI
from tictactoe.game import Game


def main() -> None:
    cli = CLI()
    game = Game(cli)
    game.play()


if __name__ == "__main__":
    main()
