from dataclasses import dataclass, field
from typing import Tuple, Union
import pygame

from lib.mover import Mover, VerticalMover


@dataclass
class ImageObject:
    screen: pygame.Surface
    img_path: str
    x: int
    y: int
    scale: int = 1
    rotate: int = 0
    colorkey: Union[Tuple[int, int, int], None] = None
    speed: int = 0
    image: pygame.Surface = field(init=False)
    mover: Mover = field(init=False)
    rect: pygame.Rect = field(init=False)

    def __post_init__(self):
        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect()
        if self.scale != 1:
            self.image = pygame.transform.scale(self.image, (self.image.get_rect().width * self.scale, self.image.get_rect().height * self.scale))
        if self.rotate != 0:
            self.image = pygame.transform.rotate(self.image, self.rotate)
        if self.colorkey:
            self.image.set_colorkey(self.colorkey)
        if self.speed:
            self.mover = VerticalMover(self.speed)

    def draw(self):
        #print(self.image.get_rect())
        self.rect = self.screen.blit(self.image, (self.x - self.image.get_rect().width/2, self.y - self.image.get_rect().height/2))

    def move_to(self, x: int, y: int):
        self.x = x
        self.y = y

    def move_delta(self, x: int, y: int):
        self.x = self.x + x
        self.y = self.y + y

    def auto_move(self):
        self.x, self.y = self.mover.move(self.x, self.y)
    
    def get_rect(self):
        return self.rect
    
    def collide_with_rect(self, rect: pygame.Rect):
        return self.get_rect().colliderect(rect)