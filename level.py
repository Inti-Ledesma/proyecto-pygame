import pygame
from configurations import tile_size,\
import_folder, time_format, fonts, health_img, lives, characters
from tiles import Tile
from characters import CharacterX, CharacterBill
from bullets import Bullet
from enemies import BallDeVoux, Spiky, GunVolt
from enemies_limits import EnemyLimit
from coin import Coin
from spike import Spike
from live import Live
from climb_limits import ClimbLimit
from player import Player

class Level:
    def __init__(self, surface, level_data, level:str):
        self.display_surface = surface
        self.surface_size = surface.get_size()
        self.level = level
        self.import_tiles(level)
        self.level_setup(self.surface_size, level_data['level_layout'], level_data['limits'])
        self.level_timer = 120
        self.level_delay = pygame.time.get_ticks()
        self.bullet_delay = pygame.time.get_ticks()
        self.stop = False
        self.character = 'x'
        self.character_change_delay = -2000
        self.player_stats = Player()
        
        # Status bar
        self.health_img = health_img
        self.lives_img = lives

    def import_tiles(self, level):
        full_path = "resources/graphics/tiles/level_" + level
        self.tileset = {'0':'','1':'','1}':'','2':'','2}':'','3':'',
                        '4':'','4}':'','5':'','5}':'','6':'','6}':'',
                        '7':'','8':'','8}':'','9':'',
                        '╔':'','╗':'','╚':'','╝':''}

        tiles_list = import_folder(full_path, (32, 32))
        for tile_index, tile in enumerate(self.tileset.keys()):
            self.tileset[tile] = tiles_list[tile_index]

    def level_setup(self, level_size, layout, lvl_limits):
        self.bg = pygame.image.load("resources/graphics/bg/" + self.level + ".png")
        self.bg = pygame.transform.scale(self.bg, level_size)

        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.live = pygame.sprite.GroupSingle()
        self.character = pygame.sprite.GroupSingle()
        self.enemy_limits = []
        self.climb_limits = []
        
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell.isnumeric() or cell == '╔' or cell == '╗' or cell == '╚' or cell == '╝':
                    climbable = False
                    if lvl_limits[row_index][col_index] == '}':
                        climbable = True
                        cell += '}'
                    tile = Tile((x,y), self.tileset[cell], climbable)
                    self.tiles.add(tile)
                else:
                    match cell:
                        case '^':
                            spike = Spike((x,y))
                            self.spikes.add(spike)
                        case 'c':
                            coin = Coin((x+16,y+16))
                            self.coins.add(coin)
                        case 'B':
                            enemy = BallDeVoux((x,y+36))
                            self.enemies.add(enemy)
                        case 'S':
                            enemy = Spiky((x,y+36))
                            self.enemies.add(enemy)
                        case 'G':
                            enemy = GunVolt((x,y+36))
                            self.enemies.add(enemy)
                        case 'L':
                            live = Live((x,y))
                            self.live.add(live)
                        case 'P':
                            player = CharacterX((x,y))
                            self.character.add(player)
                match lvl_limits[row_index][col_index]:
                    case '¡':
                        limit = ClimbLimit((x,y))
                        self.climb_limits.append(limit)
                    case '!':
                        limit = EnemyLimit((x,y))
                        self.enemy_limits.append(limit)

    def generate_bullet(self, current_time):
        character = self.character.sprite
        path = characters[self.character]['bullet_path']
        size = characters[self.character]['bullet_size']
        shoot_up = False

        if character.facing_right:
            x = character.hitbox.x + characters[self.character]['bullet_spawn_xright']
        else:
            x = character.hitbox.x + characters[self.character]['bullet_spawn_xleft']
        
        if self.character == 'bill':
            if character.crouch:
                y = character.hitbox.y + characters[self.character]['bullet_spawn_ycrouch']
            else:
                y = character.hitbox.y + characters[self.character]['bullet_spawn_y']
            
            if character.look_up:
                shoot_up = True
        else:
            y = character.hitbox.y + characters[self.character]['bullet_spawn_y']

        if current_time - self.bullet_delay > character.fire_rate and\
        character.shooting and len(self.bullets) < 6:
            self.bullets.add(Bullet((x,y), character.facing_right, shoot_up, path, size))
            self.bullet_delay = pygame.time.get_ticks()

    def status_bar(self, screen:pygame.Surface):
        character = self.character.sprite

        # Bar
        bar = pygame.Rect(0,0,screen.get_width(),64)
        pygame.draw.rect(screen, "black", bar)

        # Score
        x = 50
        score_text = "score: " + str(self.player_stats.score)
        for char in score_text:
            screen.blit(fonts[char], (x, 20))
            x += 32

        # Timer
        timer_text = time_format(self.level_timer)
        x = 550
        for char in timer_text:
            screen.blit(fonts[char], (x, 20))
            x += 32
        
        # Health
        health_text = "health:"
        x = 860
        for char in health_text:
            screen.blit(fonts[char], (x, 20))
            x += 32
        screen.blit(self.health_img, (1080, 10))
        for live in range(character.health):
            screen.blit(self.lives_img[str(live+1)]['img'], self.lives_img[str(live+1)]['pos'])
    
    def update_timer(self, current_time):
        if current_time - self.level_delay > 1000:
            self.level_timer -= 1
            self.level_delay = pygame.time.get_ticks()

    def change_character(self, current_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not self.character.sprite.pain and\
        current_time - self.character_change_delay > 2000:
            if self.character == 'x':
                self.character.add(CharacterBill(self.character.sprite.hitbox.center))
                self.character = 'bill'
            else:
                self.character.add(CharacterX(self.character.sprite.hitbox.center))
                self.character = 'x'
            self.character_change_delay = pygame.time.get_ticks()

    def run(self, current_time, editor_mode):
        if not self.stop:
            # Background
            self.display_surface.blit(self.bg, (0,0))

            # Level Tiles
            self.tiles.draw(self.display_surface)

            # Spikes
            self.spikes.draw(self.display_surface)
            self.spikes.update(self.character)

            # Coins
            self.coins.update(self.character)
            self.coins.draw(self.display_surface)

            # Enemies
            self.enemies.draw(self.display_surface)
            self.enemies.update(self.enemy_limits, self.bullets, self.character, self.tiles, self.display_surface, current_time)

            # Bullets
            self.generate_bullet(current_time)
            self.bullets.update(self.tiles, self.display_surface)
            self.bullets.draw(self.display_surface)

            # Live (regeneration)
            self.live.draw(self.display_surface)
            self.live.update(self.character)
            # Player
            if self.character == 'x':
                self.character.update(current_time, self.tiles, self.display_surface)
            else:
                self.character.update(current_time, self.tiles, self.display_surface, self.climb_limits)
            if self.character.sprite.dead:
                self.stop = True
            self.character.draw(self.display_surface)
            # Status Bar
            self.status_bar(self.display_surface)
            self.update_timer(current_time)

            self.change_character(current_time)

        if not self.stop:
            if editor_mode:
                pygame.draw.rect(self.display_surface, "green", self.character.sprite.rect, 2)
                pygame.draw.rect(self.display_surface, "red", self.character.sprite.hitbox, 2)
                for enemy in self.enemies:
                    pygame.draw.rect(self.display_surface, "green", enemy.rect, 2)
                    pygame.draw.rect(self.display_surface, "red", enemy.hitbox, 2)
                for tile in self.tiles:
                    pygame.draw.rect(self.display_surface, "cyan", tile.rect, 2)
                for bullet in self.bullets:
                    pygame.draw.rect(self.display_surface, "yellow", bullet.rect, 2)
                for limit in self.climb_limits:
                    pygame.draw.rect(self.display_surface, "cyan", limit.rect, 2)
                for coin in self.coins:
                    pygame.draw.rect(self.display_surface, "yellow", coin.rect, 2)
    
        return self.stop