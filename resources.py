import os
import pygame
import json
import sys
import ctypes


## Game board
pygame.init()
width, height = 858, 540
fpsClock = pygame.time.Clock()
WIN = pygame.display.set_mode((width, height))

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (93.3,13.3,16.1)
YELLOW = "#83d313"

TITLE_FONT = pygame.font.SysFont('comicsans', 50)
SUBTITLE_FONT = pygame.font.SysFont('comicsans', 40)
MEDIUM_FONT = pygame.font.SysFont('comicsans', 35)
SMALL_FONT = pygame.font.SysFont('comicsans', 25)
SMALLEST_FONT = pygame.font.SysFont('comicsans', 20)


## Game Values
FPS = 60
MAX_CARDS = 108
INITIAL_CARDS = 7
MAX_TURN_TIME = 30
clock = pygame.time.Clock()
small_font = pygame.font.Font(None, 30)
count_font = pygame.font.Font(None, 50)
mini_font = pygame.font.Font(None, 18)

# Player values
my_save_slot = open("save.json")
save = json.load(my_save_slot)


## App Info
icon = pygame.image.load('Assets/logo/logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Duck Hunt")


# Game Assets

# Title Screen
title_screen_bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets/background/title_screen', "background.png")), (858, 540))

# Duck Hunt

# Walking
walking_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/walking', 'walking_1.png')), (150, 150))
walking_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/walking', 'walking_2.png')), (150, 150))
walking_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/walking', 'walking_3.png')), (150, 150))
walking_4 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/walking', 'walking_4.png')), (150, 150))
walking_5 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/walking', 'walking_5.png')), (150, 150))
walking_6 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/walking', 'walking_6.png')), (150, 150))

# Jump
jump_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/jump', 'jump_1.png')), (150, 150))
jump_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/jump', 'jump_2.png')), (150, 150))
jump_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/jump', 'jump_3.png')), (150, 150))

# Shows Ducks
one_duck = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/duck', 'one_duck.png')), (150, 150))
two_ducks = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/duck', 'two_ducks.png')), (150, 150)) 

# Laughs
laughs_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/laughs', 'laughs.png')), (150, 150))
laughs_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/dog/laughs', 'laughs_2.png')), (150, 150)) 


# Ducks

# Blue

# Horizontal
blue_horizontal_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/horizontal', 'horizontal.png')), (80, 80))
blue_horizontal_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/horizontal', 'horizontal_2.png')), (80, 80))
blue_horizontal_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/horizontal', 'horizontal_3.png')), (80, 80))

# Up RIGHT
blue_up_1_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/up', 'up_right.png')), (80, 80))
blue_up_2_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/up', 'up_2_right.png')), (80, 80))
blue_up_3_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/up', 'up_3_right.png')), (80, 80))

# Up LEFT
blue_up_1_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/up', 'up_left.png')), (80, 80))
blue_up_2_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/up', 'up_2_left.png')), (80, 80))
blue_up_3_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/up', 'up_3_left.png')), (80, 80))

# Fall
blue_falling_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/falling', 'fall.png')), (80, 80))
blue_falling_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/falling', 'fall_2.png')), (80, 80))
blue_falling_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/falling', 'fall_3.png')), (80, 80))
blue_falling_4 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/falling', 'fall_4.png')), (80, 80))

# Shoot
blue_shoot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/shoot', 'shoot.png')), (80, 80))


# Green

# Horizontal
green_horizontal_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/horizontal', 'horizontal.png')), (80, 80))
green_horizontal_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/horizontal', 'horizontal_2.png')), (80, 80))
green_horizontal_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/horizontal', 'horizontal_3.png')), (80, 80))

# Up RIGHT
green_up_1_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/up', 'up_right.png')), (80, 80))
green_up_2_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/up', 'up_2_right.png')), (80, 80))
green_up_3_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/up', 'up_3_right.png')), (80, 80))

# Up LEFT
green_up_1_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/up', 'up_left.png')), (80, 80))
green_up_2_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/up', 'up_2_left.png')), (80, 80))
green_up_3_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/up', 'up_3_left.png')), (80, 80))

# Fall
green_falling_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/falling', 'fall.png')), (80, 80))
green_falling_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/falling', 'fall_2.png')), (80, 80))
green_falling_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/falling', 'fall_3.png')), (80, 80))
green_falling_4 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/falling', 'fall_4.png')), (80, 80))

# Shoot
green_shoot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/shoot', 'shoot.png')), (80, 80))


# Brown

# Horizontal
brown_horizontal_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/horizontal', 'horizontal.png')), (80, 80))
brown_horizontal_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/horizontal', 'horizontal_2.png')), (80, 80))
brown_horizontal_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/horizontal', 'horizontal_3.png')), (80, 80))

# Up RIGHT
brown_up_1_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/up', 'up_right.png')), (80, 80))
brown_up_2_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/up', 'up_2_right.png')), (80, 80))
brown_up_3_right = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/up', 'up_3_right.png')), (80, 80))

# Up LEFT
brown_up_1_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/up', 'up_left.png')), (80, 80))
brown_up_2_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/up', 'up_2_left.png')), (80, 80))
brown_up_3_left = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/up', 'up_3_left.png')), (80, 80))

# Fall
brown_falling_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/falling', 'fall.png')), (80, 80))
brown_falling_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/falling', 'fall_2.png')), (80, 80))
brown_falling_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/falling', 'fall_3.png')), (80, 80))
brown_falling_4 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/falling', 'fall_4.png')), (80, 80))

# Shoot
brown_shoot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/shoot', 'shoot.png')), (80, 80))


# Sound effect
title = pygame.mixer.Sound("assets/music/title.ogg")
intro = pygame.mixer.Sound("assets/music/intro.ogg")
gotcha = pygame.mixer.Sound("assets/music/gotcha.mp3")
dog_bark = pygame.mixer.Sound("assets/music/dog_bark.mp3")
gun_shot = pygame.mixer.Sound("assets/music/gun_shot.ogg")
falling = pygame.mixer.Sound("assets/music/falling.ogg")
lands = pygame.mixer.Sound("assets/music/lands.ogg")
show = pygame.mixer.Sound("assets/music/show.ogg")
laughs_sound = pygame.mixer.Sound("assets/music/laughs.ogg")
clear = pygame.mixer.Sound("assets/music/clear.ogg")


# Modes windows
modes_bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets/modes', "background.png")), (858, 540))
mode_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/modes', "1_duck.png")), (300, 300))
mode_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/modes', "2_duck.png")), (300, 300))
black_bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets/modes', "black.png")), (300, 300))

# Dialog
dialog = pygame.transform.scale(pygame.image.load(os.path.join('Assets/dialog', "dialog.png")), (328, 138))

# Round
round = pygame.transform.scale(pygame.image.load(os.path.join('Assets/dialog', "round.png")), (328, 138))

# Board
board_day_bg = pygame.transform.scale(pygame.image.load(os.path.join('assets/background/main_game', "background_day.png")), (858, 540)) 
board_day_blood_bg = pygame.transform.scale(pygame.image.load(os.path.join('assets/background/main_game', "background_day_blood.png")), (858, 540)) 

board_night_bg = pygame.transform.scale(pygame.image.load(os.path.join('assets/background/main_game', "background_night.png")), (858, 540)) 
board_night_blood_bg = pygame.transform.scale(pygame.image.load(os.path.join('assets/background/main_game', "background_night_blood.png")), (858, 540)) 

# Hits
hit_zero = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_zero.png")), (315, 35))
hit_one = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_one.png")), (315, 35))
hit_two = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_two.png")), (315, 35))
hit_three = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_three.png")), (315, 35))
hit_four = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_four.png")), (315, 35))
hit_five = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_five.png")), (315, 35))
hit_six = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_six.png")), (315, 35))
hit_seven = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_seven.png")), (315, 35))
hit_eight = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_eight.png")), (315, 35))
hit_nine = pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_nine.png")), (315, 35))
hit_ten =  pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/hits', "hit_ten.png")), (315, 35))

# Shots
all_shots =  pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/shots', "all_shots.png")), (52, 34))
two_shots =  pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/shots', "two_shots.png")), (52, 34))
one_shot =  pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/shots', "one_shot.png")), (52, 34))
zero_shot =  pygame.transform.scale(pygame.image.load(os.path.join('assets/dialog/shots', "zero_shot.png")), (52, 34))

# Cursor
cursor =  pygame.transform.scale(pygame.image.load(os.path.join('assets/cursor', "cursor.png")), (52, 34))
