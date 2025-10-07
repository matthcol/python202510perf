from dataclasses import dataclass


@dataclass
class Shape:
    """ represents geometric shape """

    name: str | None = None