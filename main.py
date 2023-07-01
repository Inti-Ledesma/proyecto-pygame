import pygame, sys
from configurations import *
from level import Level
from mode import *
from forms import MainMenu, LevelMenu

pygame.init()

pygame.display.set_caption("Mega Contra")
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

level = Level(screen, levels['3'], '3')
current_time = 0 
font = pygame.font.SysFont("Arial", 20)
main_menu = MainMenu(screen, 0, 0, 1280, 672, "black", "black", 1, True)
lvl_menu = LevelMenu(screen, 0, 0, 1280, 672, "black", "black", 1, True)

while 1:
    current_time = pygame.time.get_ticks()

    events_list = pygame.event.get()
    for event in events_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                set_mode()
    
    # main_menu.update(events_list)
    # lvl_menu.update(events_list)
    # if not level.run(current_time, get_mode()):
    #     pass

    pygame.display.update()
    clock.tick(60)