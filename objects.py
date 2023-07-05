import pygame
from configurations import import_folder, volume

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = import_folder("resources/graphics/coin", (16, 16))
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.score_value = 100
        self.sfx = pygame.mixer.Sound("resources/sfx/objects/coin.mp3")
        self.sfx.set_volume(volume.sfx_volume)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        
        self.image = self.animations[int(self.frame_index)]
    
    def collisions(self, player, player_stats):
        if self.rect.colliderect(player.hitbox):
            player_stats.score += self.score_value
            self.sfx.play(0)
            self.kill()
    
    def update(self, player:pygame.sprite.GroupSingle, player_stats):
        self.collisions(player.sprite, player_stats)
        self.animate()

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
        self.sfx = pygame.mixer.Sound("resources/sfx/objects/door.mp3")
        self.sfx.set_volume(volume.sfx_volume)
        self.sfx_flag = True

    def import_assets(self):
        character_path = "resources/graphics/door/"
        
        self.animations = {'static':[], 'open':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path,(64, 96))
            
    def check_key_grabbed(self, player_stats):
        if player_stats.key_grabbed:
            if self.sfx_flag:
                self.sfx.play(0)
                self.sfx_flag = False
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

class Goal(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("resources/graphics/goal/1.png")
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(topleft = pos)
    
    def check_player(self, player, player_stats):
        if self.rect.colliderect(player.hitbox):
            player_stats.end_level = True

    def update(self, player, player_stats):
        self.check_player(player.sprite, player_stats)

class Live(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = import_folder("resources/graphics/heart", (32,32))
        self.image = self.animations[0]
        self.rect = self.image.get_rect(topleft = pos)
        self.frame_index = 0
        self.animation_speed = 0.1
        self.sfx = pygame.mixer.Sound("resources/sfx/objects/live.mp3")
        self.sfx.set_volume(volume.sfx_volume)

    def animation(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animations):
            self.frame_index = 0
        
        image = self.animations[int(self.frame_index)]
        self.image = image
    
    def check_collissions(self, player, player_stats):
        # Player collision
        if self.rect.colliderect(player.hitbox):
            if player_stats.health < 3:
                player_stats.health += 1
                self.sfx.play(0)
                self.kill()
    
    def update(self, player:pygame.sprite.GroupSingle, player_stats):
        self.animation()
        self.check_collissions(player.sprite, player_stats)

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
                player.invulnerability_timer = pygame.time.get_ticks()
                player.speed = 1
    
    def update(self, player:pygame.sprite.GroupSingle, player_stats):
        self.check_collissions(player.sprite, player_stats)

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surface, climbable):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)
        self.climbable = climbable