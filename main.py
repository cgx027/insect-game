from dataclasses import dataclass
from time import sleep
import pygame

from .insects.ladybug import Ladybug


def run():
    pygame.init()
    pygame.key.set_repeat(10, 15)
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
    screen.fill([255, 255, 255])

    lady_bug = Ladybug(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    lady_bug.move_delta(10, 0)
                if event.key == pygame.K_LEFT:
                    lady_bug.move_delta(-10, 0)
                if event.key == pygame.K_DOWN:
                    lady_bug.move_delta(0, 10)
                if event.key == pygame.K_UP:
                    lady_bug.move_delta(0, -10)

                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEMOTION:
                mx, my = event.pos
                lady_bug.move_to(mx, my)

    pygame.quit()


# def draw(x: int, y: int):
#     pygame.display.flip()


if __name__ == "__main__":
    run()
