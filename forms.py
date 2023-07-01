import pygame
from GUI_button_image import *
from GUI_button import *
from GUI_checkbox import *
from GUI_form import *
from GUI_label import *
from GUI_picture_box import *
from GUI_slider import *
from GUI_textbox import *

class MainMenu(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volume = 0.2
        self.music_flag = True

        pygame.mixer.init()

        bg = PictureBox(self._slave, x, y, 1280, 672, "resources/graphics/bg/main menu.png")
        title = PictureBox(self._slave, 305, 20, 670, 340, "resources/graphics/main menu/title.png")
        bill_img = PictureBox(self._slave, 75, 292, 226, 380, "resources/graphics/main menu/bill razer image.png")
        x_img = PictureBox(self._slave, 950, 310, 224, 362, "resources/graphics/main menu/x image.png")
        btn_play = Button_Image(self._slave, x, y, 512, 400, 256, 96, "resources/graphics/GUI/button play loose.png", 
                                self.press_button, "resources/graphics/GUI/button play pressed.png")
        btn_settings = Button_Image(self._slave, x, y, 512, 520, 256, 96, "resources/graphics/GUI/button settings 1 loose.png", 
                                self.press_button, "resources/graphics/GUI/button settings 1 pressed.png")
        btn_scores = Button_Image(self._slave, x, y, 1164, 20, 96, 96, "resources/graphics/GUI/button scores loose.png", 
                                self.press_button, "resources/graphics/GUI/button scores pressed.png")

        self.lista_widgets.append(bg)
        self.lista_widgets.append(title)
        self.lista_widgets.append(bill_img)
        self.lista_widgets.append(x_img)
        self.lista_widgets.append(btn_play)
        self.lista_widgets.append(btn_settings)
        self.lista_widgets.append(btn_scores)

        # Music
        self.song = pygame.mixer.Sound("resources/music/presentation.mp3")

        # SFX
        self.sfx_btn_pressed = pygame.mixer.Sound("resources/sfx/GUI/button pressed.wav")

        self.song.set_volume(self.volume)
        self.sfx_btn_pressed.set_volume(self.volume)

    def press_button(self, path_btn_pressed):
        btn_pressed = pygame.image.load(path_btn_pressed)
        self.button_1_image = btn_pressed
        self.sfx_btn_pressed.play(0)
        return btn_pressed
    
    def update(self, lista_eventos):
        if self.active:
            if self.music_flag:
                self.song.play(0)
                self.music_flag = False
            self.draw()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)

class LevelMenu(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volume = 0.2

        bg = PictureBox(self._slave, x, y, 1280, 672, "resources/graphics/bg/level menu.png")

        interface = PictureBox(self._slave, 384, 144, 512, 400, "resources/graphics/GUI/interface level select.png")
        btn_lvl_1 = Button_Image(self._slave, x, y, 424, 320, 96, 96, "resources/graphics/GUI/button level 1 loose.png", 
                                self.press_button, "resources/graphics/GUI/button level 1 pressed.png")
        btn_lvl_2 = Button_Image(self._slave, x, y, 536, 320, 96, 96, "resources/graphics/GUI/button level 2 loose.png", 
                                self.press_button, "resources/graphics/GUI/button level 2 pressed.png")
        btn_lvl_3 = Button_Image(self._slave, x, y, 648, 320, 96, 96, "resources/graphics/GUI/button level 3 loose.png", 
                                self.press_button, "resources/graphics/GUI/button level 3 pressed.png")
        btn_boss_lvl = Button_Image(self._slave, x, y, 760, 320, 96, 96, "resources/graphics/GUI/button boss level loose.png", 
                                self.press_button, "resources/graphics/GUI/button boss level pressed.png")
        btn_scores = Button_Image(self._slave, x, y, 1164, 20, 96, 96, "resources/graphics/GUI/button scores loose.png", 
                                self.press_button, "resources/graphics/GUI/button scores pressed.png")

        self.lista_widgets.append(bg)
        self.lista_widgets.append(interface)
        self.lista_widgets.append(btn_lvl_1)
        self.lista_widgets.append(btn_lvl_2)
        self.lista_widgets.append(btn_lvl_3)
        self.lista_widgets.append(btn_boss_lvl)
        self.lista_widgets.append(btn_scores)

        # Music

        # SFX
        self.sfx_btn_pressed = pygame.mixer.Sound("resources/sfx/GUI/button pressed.wav")

        self.sfx_btn_pressed.set_volume(self.volume)

    def press_button(self, path_btn_pressed):
        btn_pressed = pygame.image.load(path_btn_pressed)
        self.button_1_image = btn_pressed
        self.sfx_btn_pressed.play(0)
        return btn_pressed

    def update(self, lista_eventos):
        if self.active:
            self.draw()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)