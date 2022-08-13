from dataclasses import dataclass
from typing import Protocol, Tuple

class Mover(Protocol):
    def move(self, x: int, y: int) -> Tuple[int, int]:
        ...

@dataclass
class VerticalMover:
    speed: int = 5

    def move(self, x, y):
        return x, y + self.speed