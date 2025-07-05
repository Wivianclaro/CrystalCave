# C
import pygame

COLOR_BLUE = (0, 35, 245)
COLOR_GREEN = (144, 238, 144)
COLOR_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Player1Idle': 3,
    'Player2Idle': 3,
    'Enemy1': 2,
    'Enemy2': 1,
    'BlueCrystal': 2,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1Idle': pygame.K_UP,
                 'Player2Idle': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1Idle': pygame.K_DOWN,
                 'Player2Idle': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1Idle': pygame.K_LEFT,
                 'Player2Idle': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1Idle': pygame.K_RIGHT,
                 'Player2Idle': pygame.K_d}
# PLAYER_KEY_SHOOT = {'Player1Idle': pygame.K_RCTRL,
#                  'Player2Idle': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
