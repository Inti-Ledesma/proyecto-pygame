import pygame
from configurations import import_folder

class Door(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_assets()
        self.status = 'static'
        self.image = self.animations[self.status][0]
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = pygame.Rect(self.rect.x+16, self.rect.y, 32, 94)
        self.frame_index = 0
        self.animation_speed = 0.1

    def import_assets(self):
        character_path = "resources/graphics/door/"
        
        self.animations = {'static':[], 'open':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path,(64, 96))
            
    def check_key_grabbed(self, player_stats):
        if player_stats.key_grabbed:
            self.status = 'open'
    
    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'open':
                self.kill()
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
    
    def update(self, player_stats):
        self.check_key_grabbed(player_stats)
        self.animate()