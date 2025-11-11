import random
from typing import Iterable

import pygame
from pygame.math import Vector2  # type: ignore[attr-defined]


FRUIT_COLOR = (126, 166, 114)
FRUIT_SIZE = 20


class Fruits:
    """Fruit entity that spawns on a grid and avoids occupied positions."""

    def __init__(
        self,
        screen_width: int = 800,
        screen_height: int = 600,
        fruit_size: int = FRUIT_SIZE,
    ) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.size = fruit_size
        self.position = Vector2(0, 0)
        self.randomize([])

    def draw(self, surface: pygame.Surface) -> None:
        rect = pygame.Rect(
            int(self.position.x),
            int(self.position.y),
            self.size,
            self.size,
        )
        pygame.draw.rect(surface, FRUIT_COLOR, rect)

    def randomize(self, occupied_positions: Iterable[Vector2]) -> None:
        occupied = set((int(p.x), int(p.y)) for p in occupied_positions)
        while True:
            x = random.randrange(0, self.screen_width, self.size)
            y = random.randrange(0, self.screen_height, self.size)
            if (x, y) not in occupied:
                self.position = Vector2(x, y)
                return


