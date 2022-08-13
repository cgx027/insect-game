from dataclasses import dataclass
from time import sleep
import pygame

from insects.ladybug import Ladybug
from objects.image_object import ImageObject

def draw_background(screen: pygame.Surface):
    screen.fill([255, 255, 255])

def run():
    pygame.init()
    pygame.key.set_repeat(10, 15)
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

    player1 = ImageObject(screen, "asserts/ladybug.png", 320, 240)

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
            
            draw_background(screen)
            player1.draw()
            pygame.display.flip()

    pygame.quit()


# def draw(x: int, y: int):
#     pygame.display.flip()


if __name__ == "__main__":
    run()
