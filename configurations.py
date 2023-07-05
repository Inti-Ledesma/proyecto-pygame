import pygame
import json
import sqlite3
from os import walk

# Volumen
class Volume():
    def __init__(self):
        self.music_volume = 0.5
        self.sfx_volume = 0.5

volume = Volume()
tile_size = 32

# Level layout
#╔  ╗  ╚  ╝

level_1 = {
    'bg':"resources/graphics/bg/1.png",
    'level_layout':[
    '                                        ',
    '                                        ',
    '777776                                  ',
    ' cKc           c                        ',
    '                                        ',
    '3333333333333334                        ',
    '╔77777777777╗╔76   c     c              ',
    '5           15                          ',
    '5   c      c15 L   0     0    c         ',
    '5          c15        S                 ',
    '5c  2334    1╚334^^^^^^^^^^^234         ',
    '5   87╗╚34  1999╚33333333333╝╔6    c    ',
    '╚4    87╗5  877777777777777776          ',
    '95  c   15c                      234    ',
    '9╚4     15c                      876   c',
    '99╚34   15c             c               ',
    '77776   15c         cc                 2',
    'ED     2╝5c   cc        24            2╝',
    'E      195c     c   00  15   B     B  19',
    'E   P 2╝95         ^^^^^1╚333333333333╝9',
    '333333╝99╚3334  23333333╝999999999999999'
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
    '         }                              ',
    '         }               !            ! ',
    '         }                              ',
    '         }                              ',
    '          ¡                             ',
    '                                        '
    ],'song':'resources/music/level_1.ogg',
    'time':120, 'best_time_score':4500
}

level_2 = {
    'bg':"resources/graphics/bg/2.png",
    'level_layout':[
    '                                        ',
    '                                        ',
    '6                        15  86         ',
    '     L                   15  D          ',
    '           c             15  cc         ',
    '4000000   234            15             ',
    '5   cc    195            15  24c        ',
    '5         195g           15  15   cccc  ',
    '5  2333333╝9╚33333334   c15  15         ',
    '5  1╔77777╗99╔7777776    15  15  233334 ',
    '5  15     19╔6   c c    015  15 c1╔7776 ',
    '5  15  cc 195            15  15  15     ',
    '5  86 c  c195            15  15  15cKc  ',
    '5      00c195         G  15  15  15 S  2',
    '5  c      195c   23333333╝5  15c 1╚3333╝',
    '5         195    8777777776  15  8777777',
    '╚3333334  1950     c    c    15         ',
    '77777776  195                15         ',
    'E c       195                15       P ',
    'E         195g              ^15  2333333',
    '3333333333╝9╚3333333333333333╝5  1999999'
    ],'limits':[
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                               ¡        ',
    '                              }         ',
    '                              }         ',
    '                              }         ',
    '                              } ¡       ',
    '                              }  }      ',
    '                              }  }      ',
    '                                 }      ',
    '                               ¡ }      ',
    '                              }  }      ',
    '                              }  }      ',
    '                              }         ',
    '                              } ¡       ',
    '                              }         ',
    '                              }         ',
    '                               ¡        '
    ],'song':'resources/music/level_2.ogg',
    'time':150, 'best_time_score':5250
}

level_3 = {
    'bg':"resources/graphics/bg/3.png",
    'level_layout':[
    '                                        ',
    '                                        ',
    '                                        ',
    '                                        ',
    '                                       P',
    '                                  233333',
    '                                  199999',
    '                                  877777',
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
    '                  U                    E',
    '3333333333333333334  2333333333333333333'
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
    'bg':"resources/graphics/bg/boss.png",
    'level_layout':[
    '                   P                    ',
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
    '                                       E',
    '3333333333         U          3333333333',
    '          33333333333333333333          ',
    '                                        '
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
    ],'song':'resources/music/boss.ogg',
    'time':120, 'best_time_score':4500
}

levels = {
    '1':level_1,
    '2':level_2,
    '3':level_3,
    'boss':boss_level
}

# # Functions
def import_folder(path:str, size:tuple):
    surfaces_list = []
    
    for _,_,img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            img_surface = pygame.image.load(full_path)
            img_surface = pygame.transform.scale(img_surface,(size)).convert_alpha()
            surfaces_list.append(img_surface)

    return surfaces_list

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

# Levels ranks and scores
def calculate_rank(best_score, player_score, hits):
    if player_score >= best_score and hits == 0:
        rank = 'S+'
    elif player_score >= int(best_score*0.9) and hits <= 1:
        rank = 'S'
    elif player_score >= int(best_score*0.8) and hits <= 1:
        rank = 'A'
    elif player_score >= int(best_score*0.65) and hits <= 2:
        rank = 'B'
    elif player_score >= int(best_score*0.5) and hits <= 2:
        rank = 'C'
    else:
        rank = 'D'
    
    return rank

def calculate_higher_rank(rank_1, rank_2):
    rtn = ''
    if rank_2:
        if rank_1 == 'S' or rank_1 == 'S+':
            if rank_2 == 'S' or rank_2 == 'S+':
                if rank_1 > rank_2:
                    rtn = 1
                elif rank_1 < rank_2:
                    rtn = 2
                else:
                    rtn = 0
            else:
                rtn = 1
        elif rank_2 == 'S' or rank_2 == 'S+':
            rtn = 2
        else:
            if rank_1 < rank_2:
                rtn = 1
            elif rank_1 > rank_2:
                rtn = 2
            else:
                rtn = 0
    else:
        rtn = 1
    
    return rtn

# Json
def create_stats_json():
    # Json existence check
    try:
        with open("player stats.json", "r"):
            create_json = False
    except Exception:
        level = {
            "score":0,
            "hits":0,
            "rank":''
        }
        data = {
            '1':level,
            '2':level,
            '3':level,
            'boss':level
        }
        with open("player stats.json", 'w') as file:
            json.dump(data, file, indent=4)

def level_stats_dict(player):
    lvl_stats = {
        'score':player.score,
        'hits':player.hits,
        'rank':player.rank
    }
    return lvl_stats

def save_level_stats(player, level):
    with open("player stats.json") as file:
        data = json.load(file)
    level_stats = level_stats_dict(player)
    save_data = False
    higher_rank = calculate_higher_rank(level_stats['rank'],
                                        data[level]['rank'])
    
    if higher_rank == 1:
        save_data = True
    elif higher_rank == 0 and\
        level_stats['score'] > data[level]['score']:
        save_data = True
    
    if save_data:
        data[level]['score'] = level_stats['score']
        data[level]['hits'] = level_stats['hits']
        data[level]['rank'] = level_stats['rank']
        with open("player stats.json", 'w') as file:
            json.dump(data, file, indent=4)
    
    return save_data

def total_score():
    with open("player stats.json") as file:
        data = json.load(file)
    
    total = 0

    for level in data:
        total += data[level]['score']

    return total

def delete_data_json():
    level = {
            "score":0,
            "hits":0,
            "rank":''
        }

    data = {
        '1':level,
        '2':level,
        '3':level,
        'boss':level
    }
    with open("player stats.json", 'w') as file:
        json.dump(data, file, indent=4)

def get_level_permissions():
    with open("player stats.json") as file:
        data = json.load(file)
    
    permissions = {
        '1':True,
        '2':False,
        '3':False,
        'boss':False,
    }

    permission = True
    for level in data:
        permissions[level] = permission
        if data[level]['rank'] == 'S+' or\
            data[level]['rank'] == 'S' or\
            data[level]['rank'] == 'A':
            permission = True
        else:
            permission = False

    return permissions

# SQL data base
def create_scores_db():
    with sqlite3.connect("scores database.db") as connection:
        try:
            sentence = '''
                        create table Scores
                        (
                            lvl1 integer,
                            lvl2 integer,
                            lvl3 integer,
                            lvlboss integer,
                            total integer
                        )
                        '''
            connection.execute(sentence)
            sentence = '''insert into Scores values(0,0,0,0,0)'''
            connection.execute(sentence)
        except Exception as e:
            pass

def update_scores_db(level, score):
    with sqlite3.connect("scores database.db") as connection:
        try:
            sentence = f'''update Scores set lvl{level} = ?'''
            connection.execute(sentence,(score,))
            total = total_score()
            sentence = '''update Scores set total = ?'''
            connection.execute(sentence,(total,))
        except Exception as e:
            print("Create scores:", e)

def delete_data_db():
    with sqlite3.connect("scores database.db") as connection:
        try:
            sentence = '''delete from Scores'''
            connection.execute(sentence)
            sentence = '''insert into Scores values(0,0,0,0,0)'''
            connection.execute(sentence)
        except Exception as e:
            print(e)

def get_all_scores():
    with sqlite3.connect("scores database.db") as connection:
        try:
            sentence = '''select * from Scores'''
            data = connection.execute(sentence)
            for fila in data:
                scores = list(fila)
        except Exception as e:
            print(e)
    return scores

# # Data collections

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
health_bar_img = pygame.image.load("resources/graphics/characters/health/bar.png")
width = health_bar_img.get_width() * 3
height = health_bar_img.get_height() * 3
health_bar_img = pygame.transform.scale(health_bar_img, (width, height))

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