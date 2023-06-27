import pygame
from os import walk

# Level layout
#╔  ╗  ╚  ╝

level_1_dict = {
    'level_layout':[
    '                                        ',
    '                                        ',
    '                                        ',
    '                c                       ',
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
    'ED     2╝5     cc       24            2╝',
    'E      195       c  00  15  B      B  19',
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
    ],'song':
    'resources/music/level_1.ogg'
}

levels = {
    '1':level_1_dict
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
health_img = pygame.image.load("resources/graphics/characters/bill/health/bar.png")
width = health_img.get_width() * 3
height = health_img.get_height() * 3
health_img = pygame.transform.scale(health_img, (width, height))

lives = {
    '1':{'img':'', 'pos':(1152, 22)},
    '2':{'img':'', 'pos':(1122, 22)},
    '3':{'img':'', 'pos':(1092, 22)}
}
live_img = pygame.image.load("resources/graphics/characters/x/health/live.png")
width = live_img.get_width() * 3
height = live_img.get_height() * 3
live_img = pygame.transform.scale(live_img, (width, height))
for live in lives.keys():
    lives[live]['img'] = live_img

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