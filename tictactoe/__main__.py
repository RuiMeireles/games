from tictactoe.cli import CLI
from tictactoe.game import Game
from tictactoe.strategy import RandomStrategy


def main() -> None:
    cli = CLI()
    game = Game(cli, num_human_players=0, strategy_cpu1=RandomStrategy())
    game.play()


if __name__ == "__main__":
    main()
