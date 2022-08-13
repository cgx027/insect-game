from dataclasses import dataclass, field
import pygame


@dataclass
class ImageObject:
    screen: pygame.Surface
    img_path: str
    x: int
    y: int
    image: pygame.Surface = field(init=False)

    def __post_init__(self):
        self.image = pygame.image.load(self.img_path)

    def draw(self):
        #print(self.image.get_rect())
        self.screen.blit(self.image, (self.x - self.image.get_rect().width/2, self.y - self.image.get_rect().height/2))

    def move_to(self, x: int, y: int):
        self.x = x
        self.y = y

    def move_delta(self, x: int, y: int):
        self.x = self.x + x
        self.y = self.y + y
