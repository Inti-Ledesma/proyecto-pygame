import pygame
from configurations import import_folder

class Live(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = import_folder("resources/graphics/heart", (32,32))
        self.image = self.animations[0]
        self.rect = self.image.get_rect(topleft = pos)
        self.frame_index = 0
        self.animation_speed = 0.1

    def animation(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        
        image = self.animations[int(self.frame_index)]
        self.image = image
    
    def check_collissions(self, player):
        # Player collision
        if self.rect.colliderect(player.hitbox):
            if player.health < 3:
                player.health += 1
                self.kill()
    
    def update(self, player:pygame.sprite.GroupSingle):
        self.animation()
        self.check_collissions(player.sprite)