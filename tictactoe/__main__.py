from tictactoe.cli import CLI
from tictactoe.game import Game
from tictactoe.strategy import RandomStrategy, LookAheadStrategy, RecursiveStrategy


def main() -> None:
    cli = CLI()
    # game = Game(cli)
    # game = Game(cli, num_human_players=0, strategy_cpu1=RecursiveStrategy(), strategy_cpu2=LookAheadStrategy())
    game = Game(
        cli, num_human_players=0, strategy_cpu1=RecursiveStrategy(), strategy_cpu2=RecursiveStrategy(max_depth=5)
    )
    game.play()


if __name__ == "__main__":
    main()
