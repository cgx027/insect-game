from random import randint
from time import sleep
from typing import Tuple
import pygame

from insects.ladybug import Ladybug
from lib.colors import BLACK, RED, WHITE
from objects.image_object import ImageObject

def draw_background(screen: pygame.Surface):
    screen.fill([255, 255, 255])

def draw_text(screen: pygame.Surface, font: pygame.font.Font, x: int, y: int, text: str, fg_color: Tuple[int, int], bg_color: Tuple[int, int]):
    t = font.render(text, True, fg_color, bg_color)
    rect = t.get_rect()
    rect.topleft = (x, y)
    screen.blit(t, rect)

def run():
    pygame.init()
    pygame.font.init()
    pygame.key.set_repeat(10, 15)
    font = pygame.font.Font(None, 200)

    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    bricks: list[ImageObject] = []

    player1 = ImageObject(screen, "asserts/ladybug.png", 320, 240)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player1.move_delta(10, 0)
                if event.key == pygame.K_LEFT:
                    player1.move_delta(-10, 0)
                if event.key == pygame.K_DOWN:
                    player1.move_delta(0, 10)
                if event.key == pygame.K_UP:
                    player1.move_delta(0, -10)

                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEMOTION:
                mx, my = event.pos
                player1.move_to(mx, my)

            if event.type == pygame.USEREVENT:
                x = randint(0, screen.get_width())
                bricks.append(ImageObject(screen, "asserts/brick.jpg", x, 0, 0.2, 90, colorkey=WHITE, speed=10))
                continue

        draw_background(screen)
        player1.draw()
        for brick in bricks:
            brick.auto_move()
            if brick.collide_with_rect(player1.get_rect()):
                # run()
                draw_text(screen, font, 100, 100, "HIT!!!", RED, WHITE)
            brick.draw()
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()


# def draw(x: int, y: int):
#     pygame.display.flip()


if __name__ == "__main__":
    run()
