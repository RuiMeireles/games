from typing import Protocol


class UI(Protocol):
    def begin_game(self) -> None:
        ...

    def end_game(self) -> None:
        ...
