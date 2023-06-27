import pygame
from configurations import import_folder

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = import_folder("resources/graphics/coin", (16, 16))
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        
        self.image = self.animations[int(self.frame_index)]
    
    def collisions(self, player):
        if self.rect.colliderect(player.hitbox):
            player.score += 100
            self.kill()
    
    def update(self, player:pygame.sprite.GroupSingle):
        self.collisions(player.sprite)
        self.animate()