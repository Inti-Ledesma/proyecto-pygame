import pygame
import random
from configurations import tile_size,import_folder, time_format,\
    fonts, health_bar_img, lives, names_initial, characters, volume,\
    calculate_rank, level_stats_dict, save_level_stats
from objects import *
from characters import *
from bullets import Bullet
from enemies import *
from player import Player
from limits import *

class Level:
    def __init__(self, surface, level_data, level:str):
        self.display_surface = surface
        self.surface_size = surface.get_size()
        self.level = level
        self.import_tiles()
        self.player = Player()
        self.best_score = level_data['best_time_score']
        self.level_timer = level_data['time']
        self.level_delay = 1000
        self.bullet_delay = 0
        self.character_name = 'x'
        self.character_change_delay = -2000
        self.stop = False
        self.level_setup(self.surface_size, level_data['level_layout'], level_data['limits'])
        self.form_flag = ''
        
        # Status bar
        self.health_bar_img = health_bar_img
        self.names_initial_dict = names_initial
        self.lives_dict = lives

        # Music
        self.music_flag = True
        pygame.mixer.music.load(level_data['song'])
        pygame.mixer.music.set_volume(volume.music_volume)
        pygame.mixer.music.play(-1)

    def import_tiles(self):
        self.tileset = {'╔':'','╗':'','╚':'','╝':'',
                        '0':'','1':'','1}':'','2':'','2}':'','3':'',
                        '4':'','4}':'','5':'','5}':'','6':'','6}':'',
                        '7':'','8':'','8}':'','9':'','10':''}

        full_path = "resources/graphics/tiles/level " + self.level
        tiles_list = import_folder(full_path, (32, 32))
        for tile_index, tile in enumerate(self.tileset.keys()):
            self.tileset[tile] = tiles_list[tile_index]

    def level_setup(self, level_size, layout, lvl_limits):
        self.bg = pygame.image.load("resources/graphics/bg/"+ self.level +".png")
        self.bg = pygame.transform.scale(self.bg, level_size)

        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.goal = pygame.sprite.Group()
        self.live = pygame.sprite.GroupSingle()
        self.character = pygame.sprite.GroupSingle()
        self.door = pygame.sprite.GroupSingle()
        self.key = pygame.sprite.GroupSingle()
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
                    elif cell == '9':
                        cell = str(random.randrange(9,11))
                    tile = Tile((x,y), self.tileset[cell], climbable)
                    self.tiles.add(tile)
                else:
                    match cell:
                        case '^':
                            spike = Spike((x,y))
                            self.spikes.add(spike)
                        case 'c':
                            coin = Coin((x+16,y+16))
                            self.best_score += coin.score_value
                            self.coins.add(coin)
                        case 'B':
                            enemy = BallDeVoux((x,y+36))
                            self.best_score += enemy.score_value
                            self.enemies.add(enemy)
                        case 'S':
                            enemy = Spiky((x,y+36))
                            self.best_score += enemy.score_value
                            self.enemies.add(enemy)
                        case 'G':
                            enemy = GunVolt((x,y+36))
                            self.best_score += enemy.score_value
                            self.enemies.add(enemy)
                        case 'E':
                            goal = Goal((x,y))
                            self.goal.add(goal)
                        case 'L':
                            live = Live((x,y))
                            self.live.add(live)
                        case 'D':
                            door = Door((x,y))
                            self.door.add(door)
                        case 'K':
                            key = Key((x,y))
                            self.key.add(key)
                        case 'P':
                            player = CharacterX((x,y-14), self.player.facing_right)
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
        path = characters[self.character_name]['bullet_path']
        size = characters[self.character_name]['bullet_size']
        shoot_up = False

        if character.facing_right:
            x = character.hitbox.x + characters[self.character_name]['bullet_spawn_xright']
        else:
            x = character.hitbox.x + characters[self.character_name]['bullet_spawn_xleft']
        
        if self.character_name == 'bill':
            if character.crouch:
                y = character.hitbox.y + characters[self.character_name]['bullet_spawn_ycrouch']
            else:
                y = character.hitbox.y + characters[self.character_name]['bullet_spawn_y']
            
            if character.look_up:
                shoot_up = True
        else:
            y = character.hitbox.y + characters[self.character_name]['bullet_spawn_y']

        if current_time - self.bullet_delay > character.fire_rate and\
        character.shooting and len(self.bullets) < 6:
            self.bullets.add(Bullet((x,y), character.facing_right, shoot_up, path, size))
            self.bullet_delay = pygame.time.get_ticks()

    def status_bar(self, screen:pygame.Surface):
        # Bar
        bar = pygame.Rect(0,0,screen.get_width(),64)
        pygame.draw.rect(screen, "black", bar)

        # Score
        x = 50
        score_text = "score: " + str(self.player.score)
        for char in score_text:
            screen.blit(fonts[char], (x, 20))
            x += 32

        # Timer
        timer_text = time_format(int(self.level_timer))
        x = 550
        for char in timer_text:
            screen.blit(fonts[char], (x, 20))
            x += 32
        
        # Health
        x = 860
        for char in "health:":
            screen.blit(fonts[char], (x, 20))
            x += 32
        screen.blit(self.health_bar_img, (1080, 10))
        screen.blit(self.names_initial_dict[self.character_name], (1188,18))
        for live in range(self.player.health):
            screen.blit(self.lives_dict[str(live+1)]['img'], self.lives_dict[str(live+1)]['pos'])

    def update_timer(self, current_time):
        if current_time - self.level_delay > 1000:
            self.level_timer -= 1
            self.level_delay = pygame.time.get_ticks()

    def change_character(self, current_time):
        keys = pygame.key.get_pressed()

        character = self.character.sprite

        if keys[pygame.K_SPACE] and not (character.pain or character.dead)\
        and current_time - self.character_change_delay > 1500:
            self.player.facing_right = self.character.sprite.facing_right
            block = False
            if self.character_name == 'x':
                for tile in self.tiles.sprites():
                    new_pos_1 = ((character.hitbox.topleft[0], character.hitbox.topleft[1]-14))
                    new_pos_2 = ((character.hitbox.topright[0], character.hitbox.topright[1]-14))

                    if tile.rect.x <= new_pos_1[0] < tile.rect.x+32 and\
                        tile.rect.y <= new_pos_1[1] < tile.rect.y+32 or\
                        tile.rect.x <= new_pos_2[0] < tile.rect.x+32 and\
                        tile.rect.y <= new_pos_2[1] < tile.rect.y+32:
                        block = True
                        break
                if not block:
                    x = self.character.sprite.hitbox.centerx
                    y = self.character.sprite.hitbox.centery - 30
                    self.character.add(CharacterBill((x,y), self.player.facing_right))
                    self.character_name = 'bill'
                    self.character_change_delay = pygame.time.get_ticks()
            else:
                for tile in self.tiles.sprites():
                    new_pos_1 = ((character.hitbox.centerx-12, character.hitbox.centery))
                    new_pos_2 = ((character.hitbox.centerx+12, character.hitbox.centery))

                    if tile.rect.x <= new_pos_1[0] < tile.rect.x+32 and\
                        tile.rect.y <= new_pos_1[1] < tile.rect.y+32 or\
                        tile.rect.x <= new_pos_2[0] < tile.rect.x+32 and\
                        tile.rect.y <= new_pos_2[1] < tile.rect.y+32:
                        block = True
                        break
                if not block:
                    x = self.character.sprite.hitbox.centerx
                    y = self.character.sprite.hitbox.centery - 9
                    self.character.add(CharacterX((x,y), self.player.facing_right))
                    self.character_name = 'x'
                    self.character_change_delay = pygame.time.get_ticks()

    def run(self, current_time, editor_mode, events_list):
        if self.form_flag != 'stats screen':
            self.form_flag = 'level'
        else:
            self.form_flag = level_stats_dict(self.player)

        if self.music_flag:
            pygame.mixer.music.set_volume(volume.music_volume)
            pygame.mixer.music.unpause()
            self.music_flag = False
        
        if not self.stop:
            for event in events_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.pause()
                        self.music_flag = True
                        self.form_flag = 'pause'

            # Background
            self.display_surface.blit(self.bg, (0,0))

            # Level Tiles
            self.tiles.draw(self.display_surface)

            # Spikes
            self.spikes.update(self.character, self.player)
            self.spikes.draw(self.display_surface)
            
            # Coins
            self.coins.update(self.character, self.player)
            self.coins.draw(self.display_surface)

            # Enemies
            self.enemies.draw(self.display_surface)
            self.enemies.update(self.enemy_limits, self.bullets, self.character,
            self.tiles, self.display_surface, current_time, self.player)

            # Bullets
            self.generate_bullet(current_time)
            self.bullets.update(self.tiles, self.display_surface)
            self.bullets.draw(self.display_surface)

            # Live (regeneration)
            self.live.draw(self.display_surface)
            self.live.update(self.character, self.player)

            # Goal
            self.goal.draw(self.display_surface)
            self.goal.update(self.character, self.player)

            # Key
            self.key.draw(self.display_surface)
            self.key.update(self.character, self.player)

            # Door
            self.door.draw(self.display_surface)
            self.door.update(self.player)

            # Player
            if self.character_name == 'x':
                self.character.update(current_time, self.tiles, self.door,
                                    self.display_surface, self.player)
            else:
                self.character.update(current_time, self.tiles, self.door,
                 self.display_surface, self.climb_limits, self.player)
                
            # Character switch
            self.change_character(current_time)
            
            # Level end
            if self.character.sprite.dead or self.level_timer == 0 or self.player.end_level:
                self.stop = True
                pygame.mixer.music.fadeout(5000)

            self.character.draw(self.display_surface)

            # Timer
            if self.level_timer > 0:
                self.update_timer(current_time)

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
                for limit in self.enemy_limits:
                    pygame.draw.rect(self.display_surface, "cyan", limit.rect, 2)
                for limit in self.climb_limits:
                    pygame.draw.rect(self.display_surface, "cyan", limit.rect, 2)
                for coin in self.coins:
                    pygame.draw.rect(self.display_surface, "yellow", coin.rect, 2)
        else:
            if self.player.end_level and self.level_timer > 0:
                self.level_timer -= 0.5
                self.player.score += 25

                # Rank calculator
                if self.level_timer == 0:
                    self.player.rank=calculate_rank(self.best_score,
                                                self.player.score,
                                                self.player.hits)
            else:
                self.player.rank = 'F'
            
            if len(self.player.rank) and type(self.form_flag) != dict:
                save_level_stats(self.player, self.level)
                self.form_flag = 'stats screen'
        
        # Status bar
        self.status_bar(self.display_surface)
        
        return self.form_flag