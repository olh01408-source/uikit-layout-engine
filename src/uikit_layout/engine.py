"""Core layout box solver."""
from dataclasses import dataclass

@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

    def area(self) -> float:
        return max(0.0, self.width) * max(0.0, self.height)
