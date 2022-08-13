from dataclasses import dataclass, field
from typing import Any
import pygame


@dataclass
class Ladybug:
    screen: pygame.Surface

    x: int = 0
    y: int = 0

    head: pygame.Rect = field(init=False)
    body: pygame.Rect = field(init=False)

    left_eye: pygame.Rect = field(init=False)
    right_eye: pygame.Rect = field(init=False)

    body_line: pygame.Rect = field(init=False)

    left_feeler_r: pygame.Rect = field(init=False)
    left_feeler_c: pygame.Rect = field(init=False)

    right_feeler_r: pygame.Rect = field(init=False)
    right_feeler_c: pygame.Rect = field(init=False)

    spot_1: pygame.Rect = field(init=False)
    spot_2: pygame.Rect = field(init=False)
    spot_3: pygame.Rect = field(init=False)
    spot_4: pygame.Rect = field(init=False)
    spot_5: pygame.Rect = field(init=False)

    def draw(self):
        self.head = pygame.draw.circle(
            self.screen, [0, 0, 0], [0 + self.x, 0 + self.y], 30, 0
        )

        # body
        self.body = pygame.draw.circle(
            self.screen, [14, 0, 0], [0 + self.x, 40 + self.y], 50, 0
        )

        # eyes
        self.left_eye = pygame.draw.circle(
            self.screen, [14, 0, 0], [65 + self.x, -15 + self.y], 5, 0
        )
        self.right_eye = pygame.draw.circle(
            self.screen, [14, 0, 0], [15 + self.x, -15 + self.y], 5, 0
        )

        # line in body
        self.body_line = pygame.draw.rect(
            self.screen, [0, 0, 0], [0 + self.x, -10 + self.y, 1, 100], 0
        )

        # left feeler
        self.left_feeler_r = pygame.draw.rect(
            self.screen, [0, 0, 0], [65 + self.x, -40 + self.y, 1, 15], 0
        )
        self.left_feeler_c = pygame.draw.circle(
            self.screen, [0, 0, 0], [65 + self.x, -40 + self.y], 3, 0
        )

        # right feeler
        self.right_feeler_r = pygame.draw.rect(
            self.screen, [0, 0, 0], [15 + self.x, -40 + self.y, 1, 15], 0
        )
        self.right_feeler_c = pygame.draw.circle(
            self.screen, [0, 0, 0], [15 + self.x, -40 + self.y], 3, 0
        )

        # spots
        self.spot_1 = pygame.draw.circle(
            self.screen, [0, 0, 0], [0 + self.x, 40 + self.y], 15, 0
        )
        self.spot_2 = pygame.draw.circle(
            self.screen, [0, 0, 0], [-25 + self.x, 65 + self.y], 15, 0
        )
        self.spot_3 = pygame.draw.circle(
            self.screen, [0, 0, 0], [25 + self.x, 65 + self.y], 15, 0
        )
        self.spot_4 = pygame.draw.circle(
            self.screen, [0, 0, 0], [-25 + self.x, 14 + self.y], 15, 0
        )
        self.spot_5 = pygame.draw.circle(
            self.screen, [0, 0, 0], [25 + self.x, 14 + self.y], 15, 0
        )

    def move_to(self, x: int, y: int):
        self.x = x
        self.y = y

        self.draw()

    def move_delta(self, x: int, y: int):
        self.x = self.x + x
        self.y = self.y + y

        self.draw()
        # screen.fill([14, 14, 14])
        # pygame.display.flip()
