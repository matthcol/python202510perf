from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override


@dataclass(kw_only=True)
class Shape(ABC): # ou ABCMeta
    """ represents geometric shape """

    name: str | None = None

    @override
    def __str__(self):
        return '?' if self.name is None else self.name

    @abstractmethod
    def translate(self, delta_x: float, delta_y: float) -> None: 
        """
        translate this shape
        """
        ...