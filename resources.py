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

TITLE_FONT = pygame.font.SysFont('comicsans', 50)
SUBTITLE_FONT = pygame.font.SysFont('comicsans', 40)
MEDIUM_FONT = pygame.font.SysFont('comicsans', 35)
SMALL_FONT = pygame.font.SysFont('comicsans', 25)


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

# Ducks

# Blue

# Horizontal
blue_horizontal_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/horizontal', 'horizontal.png')), (120, 120))
blue_horizontal_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/horizontal', 'horizontal_2.png')), (120, 120))
blue_horizontal_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/horizontal', 'horizontal_3.png')), (120, 120))

# Up
blue_up_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/up', 'up.png')), (120, 120))
blue_up_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/up', 'up_2.png')), (120, 120))
blue_up_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/up', 'up_3.png')), (120, 120))

# Fall
blue_falling_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/falling', 'fall.png')), (120, 120))
blue_falling_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/falling', 'fall_2.png')), (120, 120))
blue_falling_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/falling', 'fall_3.png')), (120, 120))
blue_falling_4 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/falling', 'fall_4.png')), (120, 120))

# Shoot
blue_shoot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/blue/shoot', 'shoot.png')), (120, 120))


# Green

# Horizontal
green_horizontal_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/horizontal', 'horizontal.png')), (120, 120))
green_horizontal_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/horizontal', 'horizontal_2.png')), (120, 120))
green_horizontal_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/horizontal', 'horizontal_3.png')), (120, 120))

# Up
green_up_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/up', 'up.png')), (120, 120))
green_up_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/up', 'up_2.png')), (120, 120))
green_up_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/up', 'up_3.png')), (120, 120))

# Fall
green_falling_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/falling', 'fall.png')), (120, 120))
green_falling_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/falling', 'fall_2.png')), (120, 120))
green_falling_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/falling', 'fall_3.png')), (120, 120))
green_falling_4 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/falling', 'fall_4.png')), (120, 120))

# Shoot
green_shoot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/green/shoot', 'shoot.png')), (120, 120))


# Brown

# Horizontal
brown_horizontal_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/horizontal', 'horizontal.png')), (120, 120))
brown_horizontal_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/horizontal', 'horizontal_2.png')), (120, 120))
brown_horizontal_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/horizontal', 'horizontal_3.png')), (120, 120))

# Up
brown_up_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/up', 'up.png')), (120, 120))
brown_up_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/up', 'up_2.png')), (120, 120))
brown_up_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/up', 'up_3.png')), (120, 120))

# Fall
brown_falling_1 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/falling', 'fall.png')), (120, 120))
brown_falling_2 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/falling', 'fall_2.png')), (120, 120))
brown_falling_3 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/falling', 'fall_3.png')), (120, 120))
brown_falling_4 = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/falling', 'fall_4.png')), (120, 120))

# Shoot
brown_shoot = pygame.transform.scale(pygame.image.load(os.path.join('assets/npc/duck/brown/shoot', 'shoot.png')), (120, 120))


# Sound effect
title = pygame.mixer.Sound("assets/music/title.mp3")
gotcha = pygame.mixer.Sound("assets/music/gotcha.mp3")


# Modes windows
modes_bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets/modes', "background.png")), (858, 540))
mode_1 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/modes', "1_duck.png")), (300, 300))
mode_2 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/modes', "2_duck.png")), (300, 300))
black_bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets/modes', "black.png")), (300, 300))

# Dialog
dialog = pygame.transform.scale(pygame.image.load(os.path.join('Assets/dialog', "dialog.png")), (328, 138))


# Board
board_bg = pygame.transform.scale(pygame.image.load(os.path.join('assets/background/main_game', "background.png")), (858, 540)) 