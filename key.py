import pygame
from configurations import import_folder

class Key(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = import_folder("resources/graphics/key", (32, 32))
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        
        self.image = self.animations[int(self.frame_index)]
    
    def collisions(self, player, player_stats):
        if self.rect.colliderect(player.hitbox):
            player_stats.key_grabbed = True
            self.kill()
    
    def update(self, player:pygame.sprite.GroupSingle, player_stats):
        self.collisions(player.sprite, player_stats)
        self.animate()