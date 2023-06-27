import pygame
from configurations import import_folder

class Spike(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = import_folder("resources/graphics/spike", (30,32))[0]
        self.rect = self.image.get_rect(topleft = pos)
    
    def check_collissions(self, player, player_stats):
        # Player collision
        if not player.invulnerable:
            if self.rect.colliderect(player.hitbox):
                player.pain = True
                player_stats.health -= 1
                player.invulnerability_timer = pygame.time.get_ticks()
                player.speed = 1
    
    def update(self, player:pygame.sprite.GroupSingle, player_stats):
        self.check_collissions(player.sprite, player_stats)