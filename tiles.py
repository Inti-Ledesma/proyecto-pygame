import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surface, climbable):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)
        self.climbable = climbable