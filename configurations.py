import pygame
from os import walk

# Level layout
#╔  ╗  ╚  ╝

level_1 = {
    'level_layout':[
    '                                        ',
    '                                        ',
    '777777777776                            ',
    ' cKc            c                       ',
    '                                        ',
    '33333333333333334                       ',
    '╔77777777777╗╔776  c     c              ',
    '5           15                          ',
    '5   c      c15 L   0     0    c         ',
    '5          c15                          ',
    '5c  2334    1╚334^^^^^^^^^^^234         ',
    '5   87╗╚34  1999╚33333333333╝╔6    c    ',
    '╚4    87╗5  877777777777777776          ',
    '95  c   15c                      234    ',
    '9╚4     15c             c        876   c',
    '99╚34   15c                             ',
    '77776   15c         cc                 2',
    'ED     2╝5c    cc       24            2╝',
    'E      195c      c  00  15  B      B  19',
    'E  P  2╝95         ^^^^^1╚333333333333╝9',
    '333333╝99╚33334  2333333╝999999999999999'
    ],'limits':[
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '           ¡                            ',
    '                                        ',
    '            }                           ',
    '          ¡ }                           ',
    '         }  }                           ',
    '         }  }                           ',
    '         }                              ',
    '         } ¡                            ',
    '         }               !            ! ',
    '         }                              ',
    '         }                              ',
    '         }                              ',
    '          ¡                             ',
    '                                        '
    ],'song':'resources/music/level_1.ogg',
    'time':120, 'best_time_score':4500
}

level_2 = {
    'level_layout':[
    '                                        ',
    '                                        ',
    '                                        ',
    ' cKc            c                       ',
    '                                        ',
    '33333333333333334                       ',
    '╔77777777777╗╔776  c     c              ',
    '5           15                          ',
    '5   c       15 L   0     0    c         ',
    '5           15                          ',
    '5c  233334  1╚334^^^^^^^^^^^234         ',
    '5   8777╗5  877╗╚33333333333╝╔6    c    ',
    '╚4      15     877777777777776          ',
    '95  c   15                       234    ',
    '9╚4     15              c        876   c',
    '99╚34   15                              ',
    '77776   15          cc                 2',
    'E      2╝5     cc       24            2╝',
    'E      195       c  00  15  B      B  19',
    'E   P 2╝95         ^^^^^1╚333333333333╝9',
    '333333╝99╚33334  2333333╝999999999999999'
    ],'limits':[
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '           ¡                            ',
    '            }                           ',
    '          ¡ }                           ',
    '         }  }                           ',
    '         }  }                           ',
    '         }                              ',
    '         } ¡                            ',
    '         }                              ',
    '         }               !            ! ',
    '         }                              ',
    '         }                              ',
    '         }                              ',
    '          ¡                             ',
    '                                        '
    ],'song':'resources/music/level_2.ogg',
    'time':120, 'best_time_score':4500
}

level_3 = {
    'level_layout':[
    '                                        ',
    '                                        ',
    '                                        ',
    ' cKc            c                       ',
    '                                        ',
    '33333333333333334                       ',
    '╔77777777777╗╔776  c     c              ',
    '5           15                          ',
    '5   c       15 L   0     0    c         ',
    '5           15                          ',
    '5c  233334  1╚334^^^^^^^^^^^234         ',
    '5   8777╗5  877╗╚33333333333╝╔6    c    ',
    '╚4      15     877777777777776          ',
    '95  c   15                       234    ',
    '9╚4     15              c        876   c',
    '99╚34   15                              ',
    '77776   15          cc                 2',
    'E      2╝5     cc       24            2╝',
    'E      195       c  00  15  B      B  19',
    'E   P 2╝95         ^^^^^1╚333333333333╝9',
    '333333╝99╚33334  2333333╝999999999999999'
    ],'limits':[
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        '
    ],'song':'resources/music/level_3.mp3',
    'time':120, 'best_time_score':4500
}

boss_level = {
    'level_layout':[
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                   P                    ',
    '3333333333333333333333333333333333333333'
    ],'limits':[
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        '
    ],'song':'resources/music/boss.ogg'
}

levels = {
    '1':level_1,
    '2':level_2,
    '3':level_3,
    'boss':boss_level
}

tile_size = 32
screen_width = 1280
screen_height = 672

def import_folder(path:str, size:tuple):
    surfaces_list = []

    for _,_,img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            img_surface = pygame.image.load(full_path)
            img_surface = pygame.transform.scale(img_surface,(size))
            surfaces_list.append(img_surface)
    
    return surfaces_list
# Functions
def time_format(number):
    mins = int(number / 60)
    mins_zeros = ''
    secs = number % 60
    secs_zeros = ''

    if mins < 10:
        mins_zeros = '0'
    if secs < 10:
        secs_zeros = '0'

    time = f"{mins_zeros}{mins}:{secs_zeros}{secs}"
    return time

# Data collections

# Font
fonts = {
    '0':'','1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':'',
    'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':'','j':'',
    'k':'','l':'','m':'','n':'','o':'','p':'','q':'','r':'','s':'','t':'',
    'u':'','v':'','w':'','x':'','y':'','z':'','!':'','?':'',',':'','.':'',
    '"':'',':':'','#':'','$':'','-':'','+':'','*':'','/':'','%':'','=':'',
    '(':'',')':'','[':'',']':'', ' ':''
}

list_of_fonts = import_folder("resources/graphics/font", (32,24))

for font_index,font in enumerate(fonts):
    fonts[font] = list_of_fonts[font_index]

# Health
health_img = pygame.image.load("resources/graphics/characters/health/bar.png")
width = health_img.get_width() * 3
height = health_img.get_height() * 3
health_img = pygame.transform.scale(health_img, (width, height))

lives = {
    '1':{'img':'', 'pos':(1152, 22)},
    '2':{'img':'', 'pos':(1122, 22)},
    '3':{'img':'', 'pos':(1092, 22)}
}
live_img = pygame.image.load("resources/graphics/characters/health/live.png")
width = live_img.get_width() * 3
height = live_img.get_height() * 3
live_img = pygame.transform.scale(live_img, (width, height))
for live in lives.keys():
    lives[live]['img'] = live_img

names_initial = {
    'x':'',
    'bill':''
}

name_initial_img = pygame.image.load("resources/graphics/characters/health/x.png")
width = name_initial_img.get_width() * 3
height = name_initial_img.get_height() * 3
names_initial['x'] = pygame.transform.scale(name_initial_img, (width, height))

name_initial_img = pygame.image.load("resources/graphics/characters/health/b.png")
width = name_initial_img.get_width() * 3
height = name_initial_img.get_height() * 3
names_initial['bill'] = pygame.transform.scale(name_initial_img, (width, height))


# Characters

x_dict = {
    'bullet_path':"resources/graphics/characters/x/bullet",
    'bullet_size':(16,12),
    'bullet_spawn_xright':24,
    'bullet_spawn_xleft':10,
    'bullet_spawn_y':27
}

bill_dict = {
    'bullet_path':"resources/graphics/characters/bill/bullet",
    'bullet_size':(12,12),
    'bullet_spawn_xright':12,
    'bullet_spawn_xleft':0,
    'bullet_spawn_y':27,
    'bullet_spawn_ycrouch':67
}

characters = {
    'x':x_dict,
    'bill':bill_dict
}