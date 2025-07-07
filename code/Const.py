# C
import pygame

C_BLUE = (0, 35, 245)
C_GREEN = (144, 238, 144)
C_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level2Bg0': 0,
    'Level2Bg1': 2,
    'Level2Bg2': 1,
    'Level2Bg3': 4,
    'Level2Bg4': 5,
    'Player1Idle': 3,
    'Player2Idle': 3,
    'Enemy1': 8,
    'Enemy2': 8,
    'Crystal': 8,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1Idle': 300,
    'Player2Idle': 300,
    'Enemy1': 1,
    'Enemy2': 1,
    'Crystal': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1Idle': 1,
    'Player2Idle': 1,
    'Enemy1': 50,
    'Enemy2': 50,
    'Crystal': 0,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1Idle': 0,
    'Player2Idle': 0,
    'Enemy1': 100,
    'Enemy2': 125,
    'Crystal': 200,
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

# S
SPAWN_TIME = 1000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2,50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }