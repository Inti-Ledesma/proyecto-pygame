import pygame, sys
from configurations import *
from level import Level
from mode import *

pygame.init()

pygame.display.set_caption("Mega Contra")
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

level = Level(screen, levels['1'], '1')
current_time = 0
font = pygame.font.SysFont("Arial", 20)
# song = pygame.mixer.Sound("resources/level_1.ogg")
# song.set_volume(0.1)
# song.play(-1)

while 1:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                set_mode()
    
    if not level.run(current_time, get_mode()):
        # fps_text = f"{clock.get_fps():.1f}"
        # fps_text = font.render(fps_text, True, "green")
        # screen.blit(fps_text, (10,10))
        pass

    pygame.display.update()
    clock.tick(60)