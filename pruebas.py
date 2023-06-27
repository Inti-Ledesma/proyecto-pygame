# import pygame, sys
# from configurations import screen_height, screen_width, fonts

# pygame.init()

# pygame.display.set_caption("Mega Contra")
# screen = pygame.display.set_mode((screen_width, screen_height))
# clock = pygame.time.Clock()
# x = 0
# y = 0
# contador = 0

# while True:
#     current_time = pygame.time.get_ticks()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     if contador == 0:
#         for font in fonts:
#             contador += 1
#             screen.blit(fonts[font], (x,y))
#             x += 35
#             if x == 630:
#                 y += 25
#                 x = 0

#     pygame.display.update()
#     clock.tick(60)

if 5 < 10 > 20:
    print("Lol")