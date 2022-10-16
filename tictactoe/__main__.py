from tictactoe.cli import CLI
from tictactoe.game import Game
from tictactoe.strategy import LookAheadStrategy


def main() -> None:
    cli = CLI()
    game = Game(cli, num_human_players=1, strategy_cpu1=LookAheadStrategy())
    game.play()


if __name__ == "__main__":
    main()
