import pygame, sys
from mode import *

pygame.init()
pygame.display.set_caption("Mega Contra")
pygame.display.set_icon(pygame.image.load("resources/graphics/GUI/icon.png"))
screen_w = 1280
screen_h = 672
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()

from configurations import levels, create_stats_json
from level import Level
from forms import MainMenu, LevelMenu, PauseMenu,\
    Settings, StatsScreen, HowToPlayMenu

create_stats_json()
current_time = 0
main_menu = MainMenu(screen,0,0,screen_w,screen_h,"black","black",1,False)
lvl_menu = LevelMenu(screen,0,0,screen_w,screen_h,"black","black",1,False)
pause_menu = PauseMenu(screen,0,0,screen_w,screen_h,"black","black",1,False)
settings_menu = Settings(screen,0,0,screen_w,screen_h,"black","black",1,False)
stats_screen = StatsScreen(screen,0,0,screen_w,screen_h,"black","black",1,False)
htp_menu = HowToPlayMenu(screen,0,0,screen_w,screen_h,"black","black",1,False)
lvl_form = ''
lvl_selected = ''
open_form_flag = True
forms_list = ['main menu']
form_pos = 0

while 1:
    events_list = pygame.event.get()
    for event in events_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                set_mode()

    current_form = forms_list[form_pos]

    match current_form:
        case 'main menu':
            if open_form_flag:
                main_menu.open()
                open_form_flag = False
            current_form = main_menu.update(events_list)
            if current_form != 'main menu':
                forms_list.append(current_form)
                form_pos += 1
                open_form_flag = True
                main_menu.close()
                main_menu.update(events_list)
        case 'level menu':
            if open_form_flag:
                lvl_menu.open()
                open_form_flag = False
            current_form = lvl_menu.update(events_list)
            if current_form != 'level menu':
                if current_form != 'back':
                    forms_list.append(current_form)
                    form_pos += 1
                else:
                    forms_list.pop()
                    form_pos -= 1
                open_form_flag = True
                lvl_menu.close()
                lvl_selected = lvl_menu.update(events_list)
        case 'level':
            if open_form_flag:
                lvl_form = Level(screen,levels[lvl_selected],lvl_selected)
                open_form_flag = False
            current_form = lvl_form.run(pygame.time.get_ticks(), get_mode(), events_list)
            if current_form != 'level':
                forms_list.append(current_form)
                form_pos += 1
                level_stats = lvl_form.run(pygame.time.get_ticks(), get_mode(), events_list)
                open_form_flag = True
        case 'settings':
            if open_form_flag:
                settings_menu.open()
                open_form_flag = False
            current_form = settings_menu.update(events_list)
            if current_form == 'back':
                forms_list.pop()
                form_pos -= 1
                settings_menu.close()
                settings_menu.update(events_list)
                open_form_flag = True
        case 'pause':
            if open_form_flag:
                pause_menu.open()
                open_form_flag = False
            current_form = pause_menu.update(events_list)
            if current_form != 'pause':
                if current_form == 'level':
                    forms_list.pop()
                    form_pos -= 1
                elif current_form == 'level menu':
                    forms_list.pop()
                    forms_list.pop()
                    form_pos -= 2
                    open_form_flag = True
                else:
                    forms_list.append(current_form)
                    form_pos += 1
                    open_form_flag = True
                
                pause_menu.close()
                pause_menu.update(events_list)
        case 'stats screen':
            if open_form_flag:
                stats_screen.open()
                open_form_flag = False
            current_form = stats_screen.update(events_list, level_stats)
            if current_form != 'stats screen':
                forms_list.pop()
                forms_list.pop()
                form_pos -= 2
                open_form_flag = True
                stats_screen.close()
                stats_screen.update(events_list, level_stats)
        case 'htp':
            if open_form_flag:
                htp_menu.open()
                open_form_flag = False
            current_form = htp_menu.update(events_list)
            if current_form != 'htp':
                forms_list.pop()
                form_pos -= 1
                open_form_flag = True
                htp_menu.close()
                htp_menu.update(events_list)

    pygame.display.update()
    clock.tick(60)