import pygame
from configurations import levels, volume
from GUI_button_image import *
from GUI_button import *
from GUI_checkbox import *
from GUI_form import *
from GUI_label import *
from GUI_picture_box import *
from GUI_slider import *
from GUI_textbox import *

####################################################################################################################################

class MainMenu(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.form_flag = ''

        bg = PictureBox(self._slave, x, y, 1280, 672, "resources/graphics/bg/main menu.png")
        title = PictureBox(self._slave, 305, 20, 670, 340, "resources/graphics/main menu/title.png")
        bill_img = PictureBox(self._slave, 75, 292, 226, 380, "resources/graphics/main menu/bill razer image.png")
        x_img = PictureBox(self._slave, 950, 310, 224, 362, "resources/graphics/main menu/x image.png")
        btn_play = Button_Image(self._slave, x, y, 512, 450, 256, 112, "resources/graphics/GUI/button play 1 loose.png", 
                            self.press_button, ["resources/graphics/GUI/button play 1 pressed.png", 'level menu'])
        btn_htp = Button_Image(self._slave, x, y, 1164, 20, 96, 112, "resources/graphics/GUI/button HTP loose.png", 
                            self.press_button, ["resources/graphics/GUI/button HTP pressed.png", 'htp'])

        self.widgets_dict['bg'] = bg
        self.widgets_dict['title'] = title
        self.widgets_dict['bill_img'] = bill_img
        self.widgets_dict['x_img'] = x_img
        self.widgets_dict['btn play'] = btn_play
        self.widgets_dict['btn htp'] = btn_htp

        # Music
        self.song = pygame.mixer.Sound("resources/music/presentation2.mp3")

        # SFX
        self.sfx_btn_pressed = pygame.mixer.Sound("resources/sfx/GUI/button pressed.mp3")

        self.sounds_flag = True

    def press_button(self, path_btn_pressed, key):
        btn_pressed = pygame.image.load(path_btn_pressed)
        self.sfx_btn_pressed.play(0)

        self.form_flag = key

        return btn_pressed
    
    def update(self, events_list):
        if self.active:
            self.form_flag = 'main menu'
            if self.sounds_flag:
                self.song.set_volume(volume.music_volume)
                self.sfx_btn_pressed.set_volume(volume.sfx_volume)
                self.song.play(0,0,200)
                self.sounds_flag = False
            self.draw()
            for widget in self.widgets_dict:
                self.widgets_dict[widget].update(events_list)
        else:
            self.song.stop()
            self.sounds_flag = True
            for widget in self.widgets_dict:
                if widget.rfind('btn') != -1 and self.widgets_dict[widget].isclicked:
                    self.widgets_dict[widget]._slave = self.widgets_dict[widget].image
                else:
                    self.widgets_dict[widget].update(events_list)
        
        return self.form_flag
    
####################################################################################################################################

class LevelMenu(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.form_flag = ''

        bg = PictureBox(self._slave, x, y, 1280, 672, "resources/graphics/bg/level menu.png")
        btn_back = Button_Image(self._slave, x, y, 20, 20, 96, 112, "resources/graphics/GUI/button back loose.png", 
                                self.press_button, ["resources/graphics/GUI/button back pressed.png", 'back'])
        btn_leaderboard = Button_Image(self._slave, x, y, 1164, 20, 96, 112, "resources/graphics/GUI/button leaderboard loose.png", 
                                self.press_button, ["resources/graphics/GUI/button leaderboard pressed.png", 'leaderboard'])
        btn_settings = Button_Image(self._slave, x, y, 1164, 150, 96, 112, "resources/graphics/GUI/button settings 2 loose.png", 
                                self.press_button, ["resources/graphics/GUI/button settings 2 pressed.png", 'settings'])
        interface = PictureBox(self._slave, 384, 144, 512, 400, "resources/graphics/GUI/interface level select.png")
        btn_lvl_1 = Button_Image(self._slave, x, y, 424, 320, 96, 112, "resources/graphics/GUI/button level 1 loose.png", 
                                self.press_button, ["resources/graphics/GUI/button level 1 pressed.png", '1'])
        btn_lvl_2 = Button_Image(self._slave, x, y, 536, 260, 96, 112, "resources/graphics/GUI/button level 2 loose.png", 
                                self.press_button, ["resources/graphics/GUI/button level 2 pressed.png", '2'])
        btn_lvl_3 = Button_Image(self._slave, x, y, 648, 260, 96, 112, "resources/graphics/GUI/button level 3 loose.png", 
                                self.press_button, ["resources/graphics/GUI/button level 3 pressed.png", '3'])
        btn_boss_lvl = Button_Image(self._slave, x, y, 760, 320, 96, 112, "resources/graphics/GUI/button boss level loose.png", 
                                self.press_button, ["resources/graphics/GUI/button boss level pressed.png", 'boss'])
        btn_play = Button_Image(self._slave, x, y, 592, 380, 96, 112, "resources/graphics/GUI/button play 2 loose.png", 
                                self.press_button, ["resources/graphics/GUI/button play 2 pressed.png", 'level'])

        self.widgets_dict['bg'] = bg
        self.widgets_dict['btn back'] = btn_back
        self.widgets_dict['btn leaderboard'] = btn_leaderboard
        self.widgets_dict['btn settings'] = btn_settings
        self.widgets_dict['interface'] = interface
        self.widgets_dict['btn lvl 1'] = btn_lvl_1
        self.widgets_dict['btn lvl 2'] = btn_lvl_2
        self.widgets_dict['btn lvl 3'] = btn_lvl_3
        self.widgets_dict['btn boss lvl'] = btn_boss_lvl
        self.widgets_dict['btn play'] = btn_play

        # Music
        self.music_dict = {
            'menu':pygame.mixer.Sound("resources/music/level menu.mp3"),
            '1':pygame.mixer.Sound(levels['1']['song']),
            '2':pygame.mixer.Sound(levels['2']['song']),
            '3':pygame.mixer.Sound(levels['3']['song']),
            'boss':pygame.mixer.Sound(levels['boss']['song'])
        }
        self.song = self.music_dict['menu']
        self.song_name = "menu"

        # SFX
        self.sfx_btn_pressed = pygame.mixer.Sound("resources/sfx/GUI/button pressed.mp3")

        self.sounds_flag = True

    def press_button(self, path_btn_pressed, key):
        btn_pressed = pygame.image.load(path_btn_pressed)
        self.sfx_btn_pressed.play(0)

        if key != 'back' and key != 'leaderboard' and key != 'settings' and key != 'level':
            if self.song_name != key:
                self.song.fadeout(200)
                
                self.widgets_dict['bg'] = PictureBox(self._slave, 0, 0, 1280, 672, levels[key]['bg'])
                self.song_name = key
                self.song = self.music_dict[self.song_name]

                self.song.set_volume(volume.music_volume)
                self.song.play(-1, 0, 200)
        else:
            if key == 'level' and self.song_name == 'menu':
                print("No level selected")
            else:
                self.form_flag = key

        return btn_pressed

    def update(self, events_list):
        if self.active:
            self.form_flag = 'level menu'
            if self.sounds_flag:
                self.song.set_volume(volume.music_volume)
                self.sfx_btn_pressed.set_volume(volume.sfx_volume)
                self.song.play(-1,0,200)
                self.sounds_flag = False
            self.draw()
            for widget in self.widgets_dict:
                self.widgets_dict[widget].update(events_list)
        else:
            self.song.stop()
            self.sounds_flag = True
            self.widgets_dict['bg'] = PictureBox(self._slave, 0, 0, 1280, 672, "resources/graphics/bg/level menu.png")
        
            if self.form_flag == 'level':
                self.form_flag = self.song_name
            
            self.song_name = 'menu'
            self.song = self.music_dict[self.song_name]

            for widget in self.widgets_dict:
                if widget.rfind('btn') != -1 and self.widgets_dict[widget].isclicked:
                    self.widgets_dict[widget]._slave = self.widgets_dict[widget].image
                else:
                    self.widgets_dict[widget].update(events_list)

        return self.form_flag
    
####################################################################################################################################

class Settings(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.form_flag = ''

        bg = PictureBox(self._slave, x, y, 1280, 672, "resources/graphics/bg/main menu.png")
        btn_back = Button_Image(self._slave, x, y, 20, 20, 96, 112, "resources/graphics/GUI/button back loose.png", 
                                self.press_button, ["resources/graphics/GUI/button back pressed.png", 'back'])
        interface = PictureBox(self._slave, 384, 144, 512, 400, "resources/graphics/GUI/interface settings.png")
        music_vol = Slider(self._slave, x, y, 410, 450, 100, 10, volume.music_volume, "blue", "white")
        sfx_vol = Slider(self._slave, x, y, 650, 450, 100, 10, volume.sfx_volume, "blue", "white")
        label_music_vol = Label(self._slave, 530, 425, 96, 64, str(volume.music_volume), "Arial black", 30, "black", "resources/graphics/GUI/table 1.png")
        label_sfx_vol = Label(self._slave, 770, 425, 96, 64, str(volume.music_volume), "Arial black", 30, "black", "resources/graphics/GUI/table 1.png")
        btn_test = Button_Image(self._slave, x, y, 670, 550, 96, 112, "resources/graphics/GUI/button default 2 loose.png", 
                                self.press_button, ["resources/graphics/GUI/button default 2 pressed.png", 'default'])
        self.widgets_dict['bg'] = bg
        self.widgets_dict['btn back'] = btn_back
        self.widgets_dict['interface'] = interface
        self.widgets_dict['music vol'] = music_vol
        self.widgets_dict['sfx vol'] = sfx_vol
        self.widgets_dict['label music vol'] = label_music_vol
        self.widgets_dict['label sfx vol'] = label_sfx_vol
        self.widgets_dict['btn test'] = btn_test

        # Music
        self.song = pygame.mixer.Sound("resources/music/settings and htp.mp3")

        # SFX
        self.sfx_btn_pressed = pygame.mixer.Sound("resources/sfx/GUI/button pressed.mp3")

        self.sounds_flag = True
    
    def press_button(self, path_btn_pressed, key):
        btn_pressed = pygame.image.load(path_btn_pressed)
        self.sfx_btn_pressed.play(0)
        self.form_flag = key

        return btn_pressed

    def update(self, events_list):
        if self.active:
            self.form_flag = 'settings'
            if self.sounds_flag:
                self.song.set_volume(volume.music_volume)
                self.sfx_btn_pressed.set_volume(volume.sfx_volume)
                self.song.play(-1,0,200)
                self.sounds_flag = False
            self.draw()
            for widget in self.widgets_dict:
                self.widgets_dict[widget].update(events_list)

            volume.music_volume = self.widgets_dict['music vol'].get_value()
            self.widgets_dict['label music vol'].set_text(f"{round(volume.music_volume*101)}")
            volume.sfx_volume = self.widgets_dict['sfx vol'].get_value()
            self.widgets_dict['label sfx vol'].set_text(f"{round(volume.sfx_volume*101)}")

            self.song.set_volume(volume.music_volume)
            self.sfx_btn_pressed.set_volume(volume.sfx_volume)
        else:
            self.song.stop()
            self.sounds_flag = True

            for widget in self.widgets_dict:
                if widget.rfind('btn') != -1 and self.widgets_dict[widget].isclicked:
                    self.widgets_dict[widget]._slave = self.widgets_dict[widget].image
                else:
                    self.widgets_dict[widget].update(events_list)
            
        return self.form_flag

####################################################################################################################################

class PauseMenu(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        
        self.form_flag = ''

        bg = PictureBox(self._slave, x, y, 1280, 672, "resources/graphics/bg/main menu.png")
        btn_settings = Button_Image(self._slave, x, y, 1164, 20, 96, 112, "resources/graphics/GUI/button settings 2 loose.png", 
                                self.press_button, ["resources/graphics/GUI/button settings 2 pressed.png", 'settings'])
        interface = PictureBox(self._slave, 384, 144, 512, 400, "resources/graphics/GUI/interface pause.png")
        btn_play = Button_Image(self._slave, x, y, 496, 380, 96, 112, "resources/graphics/GUI/button play 2 loose.png", 
                                self.press_button, ["resources/graphics/GUI/button play 2 pressed.png", 'level'])
        btn_lvl_menu = Button_Image(self._slave, x, y, 688, 380, 96, 112, "resources/graphics/GUI/button levels loose.png", 
                                self.press_button, ["resources/graphics/GUI/button levels pressed.png", 'level menu'])
        
        self.widgets_dict['bg'] = bg
        self.widgets_dict['btn settings'] = btn_settings
        self.widgets_dict['interface'] = interface
        self.widgets_dict['btn play'] = btn_play
        self.widgets_dict['btn lvl menu'] = btn_lvl_menu

        # Music
        self.song = pygame.mixer.Sound("resources/music/pause.mp3")

        # SFX
        self.sfx_btn_pressed = pygame.mixer.Sound("resources/sfx/GUI/button pressed.mp3")

        self.sounds_flag = True
    
    def press_button(self, path_btn_pressed, key):
        btn_pressed = pygame.image.load(path_btn_pressed)
        self.sfx_btn_pressed.play(0)
        self.form_flag = key

        return btn_pressed
    
    def update(self, events_list):
        if self.active:
            self.form_flag = 'pause'
            if self.sounds_flag:
                self.song.set_volume(volume.music_volume)
                self.sfx_btn_pressed.set_volume(volume.sfx_volume)
                self.song.play(-1,0,200)
                self.sounds_flag = False
            self.draw()
            for widget in self.widgets_dict:
                self.widgets_dict[widget].update(events_list)
        else:
            self.song.stop()
            self.sounds_flag = True

            for widget in self.widgets_dict:
                if widget.rfind('btn') != -1 and self.widgets_dict[widget].isclicked:
                    self.widgets_dict[widget]._slave = self.widgets_dict[widget].image
                else:
                    self.widgets_dict[widget].update(events_list)

        return self.form_flag
    
####################################################################################################################################

class StatsScreen(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.form_flag = ''

        bg = PictureBox(self._slave, x, y, 1280, 672, "resources/graphics/bg/main menu.png")
        interface = PictureBox(self._slave, 384, 104, 512, 400, "resources/graphics/GUI/interface stats.png")

        self.widgets_dict['bg'] = bg
        self.widgets_dict['interface'] = interface

        # Stats
        self.level_stats = {}
        self.stats_delay = 0
        self.stats_counter = 0

        # SFX
        self.sfx_dict = {
            'drumroll':pygame.mixer.Sound("resources/sfx/rank/drumroll.mp3"),
            'great':pygame.mixer.Sound("resources/sfx/rank/crowd cheer.mp3"),
            'decent':pygame.mixer.Sound("resources/sfx/rank/decent.mp3"),
            'fail':pygame.mixer.Sound("resources/sfx/rank/fail.mp3"),
            'btn pressed':pygame.mixer.Sound("resources/sfx/GUI/button pressed.mp3")
        }

        self.sfx_btn_pressed = self.sfx_dict['btn pressed']
        self.effect = self.sfx_dict['drumroll']
        self.sounds_flag = True
        self.sfx_flag = True
        self.sfx_delay = 0

    def press_button(self, path_btn_pressed, key):
        btn_pressed = pygame.image.load(path_btn_pressed)
        self.sfx_btn_pressed.play(0)
        self.form_flag = key

        return btn_pressed
    
    def play_rank_sound_effect(self, current_time):
        if current_time > self.sfx_delay + 5500:
            if self.level_stats['rank'] == 'F' or\
                self.level_stats['rank'] == 'D':
                self.effect = self.sfx_dict['fail']
            elif self.level_stats['rank'] == 'S' or\
                self.level_stats['rank'] == 'S+':
                self.effect = self.sfx_dict['great']
            else:
                self.effect = self.sfx_dict['decent']
            self.sounds_flag = True
            self.sfx_flag = False
    
    def display_level_stats(self, current_time):
        if current_time > self.stats_delay + 1850:
            match self.stats_counter:
                case 1:
                    label_score = Label(self._slave, 570, 260, 96, 64,
                        str(self.level_stats['score']),"Arial black", 30, 
                        "black", "resources/graphics/GUI/table 1.png")
                    self.widgets_dict['score'] = label_score
                case 2:
                    label_hits = Label(self._slave, 530, 370, 96, 64,
                        str(self.level_stats['hits']),"Arial black", 30, 
                        "black", "resources/graphics/GUI/table 1.png")
                    self.widgets_dict['hits'] = label_hits
                case 3:
                    rank_img = PictureBox(self._slave, 630, 212, 256, 256,
                        f"resources/graphics/ranks/{self.level_stats['rank']}.png")
                    self.widgets_dict['rank'] = rank_img
                    btn_lvl_menu = Button_Image(self._slave, 0, 0, 592, 520, 96, 112, 
                        "resources/graphics/GUI/button levels loose.png", self.press_button,
                        ["resources/graphics/GUI/button levels pressed.png", 'level menu'])
                    self.widgets_dict['btn lvl menu'] = btn_lvl_menu

            self.stats_delay = pygame.time.get_ticks()
            self.stats_counter += 1

    def update(self, events_list, lvl_stats):
        if self.active:
            self.form_flag = 'stats screen'
            if self.sounds_flag:
                self.level_stats = lvl_stats
                self.sfx_btn_pressed.set_volume(volume.sfx_volume)
                self.effect.set_volume(volume.sfx_volume)
                self.effect.play(0)
                self.sfx_delay = pygame.time.get_ticks()
                self.stats_delay = 0
                self.sounds_flag = False
            elif self.sfx_flag:
                self.play_rank_sound_effect(pygame.time.get_ticks())
            
            self.display_level_stats(pygame.time.get_ticks())

            self.draw()
            for widget in self.widgets_dict:
                self.widgets_dict[widget].update(events_list)
        else:
            self.effect.stop()
            self.sounds_flag = True
            self.sfx_flag = True
            self.stats_counter = 0
            self.effect = self.sfx_dict['drumroll']

            self.widgets_dict.pop('score')
            self.widgets_dict.pop('hits')
            self.widgets_dict.pop('rank')
            self.widgets_dict.pop('btn lvl menu')

            for widget in self.widgets_dict:
                if widget.rfind('btn') != -1 and self.widgets_dict[widget].isclicked:
                    self.widgets_dict[widget]._slave = self.widgets_dict[widget].image
                else:
                    self.widgets_dict[widget].update(events_list)
        
        return self.form_flag

####################################################################################################################################

class HowToPlayMenu(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.form_flag = ''

        bg = PictureBox(self._slave, x, y, 1280, 672, "resources/graphics/bg/main menu.png")
        interface = PictureBox(self._slave, 384, 144, 512, 400, "resources/graphics/GUI/interface HTP.png")
        btn_back = Button_Image(self._slave, x, y, 20, 20, 96, 112, "resources/graphics/GUI/button back loose.png", 
                                self.press_button, ["resources/graphics/GUI/button back pressed.png", 'back'])

        self.widgets_dict['bg'] = bg
        self.widgets_dict['btn_back'] = btn_back
        self.widgets_dict['interface'] = interface

        # Music
        self.song = pygame.mixer.Sound("resources/music/settings and htp.mp3")

        # SFX
        self.sfx_btn_pressed = pygame.mixer.Sound("resources/sfx/GUI/button pressed.mp3")

        self.sounds_flag = True
    
    def press_button(self, path_btn_pressed, key):
        btn_pressed = pygame.image.load(path_btn_pressed)
        self.sfx_btn_pressed.play(0)
        self.form_flag = key

        return btn_pressed

    def update(self, events_list):
        if self.active:
            self.form_flag = 'htp'
            if self.sounds_flag:
                self.song.set_volume(volume.sfx_volume)
                self.sfx_btn_pressed.set_volume(volume.sfx_volume)
                self.song.play(-1,0,200)
                self.sounds_flag = False
            self.draw()
            for widget in self.widgets_dict:
                self.widgets_dict[widget].update(events_list)
        else:
            self.song.stop()
            self.sounds_flag = True

            for widget in self.widgets_dict:
                if widget.rfind('btn') != -1 and self.widgets_dict[widget].isclicked:
                    self.widgets_dict[widget]._slave = self.widgets_dict[widget].image
                else:
                    self.widgets_dict[widget].update(events_list)
        
        return self.form_flag

        
