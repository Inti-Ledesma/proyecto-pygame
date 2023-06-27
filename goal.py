import pygame

class Goal(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("resources/graphics/goal/1.png")
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
        self.end_level = False
    
    def check_player(self, player):
        if self.rect.colliderect(player.hitbox):
            self.end_level = True

    def update(self, player):
        self.check_player(player.sprite)