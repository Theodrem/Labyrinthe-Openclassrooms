import pygame

"""
player controls
"""

RIGHT = "d"
LEFT = "g"
UP = "h"
DOWN = "b"
INVENTORY_BUTTON = "i"

"""
file prison.txt properties
"""
FILE_NAME = "prison.txt"
DIRECTORY_MAP = "cartes"

"""
Sprites and maze properties back 
"""
WALL = "O"
PATH = " "
MCGIVER = "X"
OBJECTS = "A", "B", "C"
OBJECT_1 = "A"
OBJECT_2 = "B"
OBJECT_3 = "C"
GUARD = "G"
EXIT = "U"

"""
Properties pygame front
"""
WIDTH_WINDOWS = 600
HEIGHT_WINDOWS = 600

SIZE_SPRITE = 40

"""
image pygame
"""

HOMEPAGE = pygame.image.load("assets/fond.jpg")

HOMEPAGE_BANNER = pygame.image.load("assets/scientist.png")
HOMEPAGE_BANNER = pygame.transform.scale(HOMEPAGE_BANNER, (300, 300))

HOMEPAGE_BUTTON = pygame.image.load("assets/button.png")
HOMEPAGE_BUTTON = pygame.transform.scale(HOMEPAGE_BUTTON, (370, 150))

GAME_OVER_IMAGE = pygame.image.load("assets/game_over.png")
GAME_OVER_IMAGE = pygame.transform.scale(GAME_OVER_IMAGE, (150, 150))

WIN_IMAGE = pygame.image.load("assets/win.png")
WIN_IMAGE = pygame.transform.scale(WIN_IMAGE, (150, 150))

WELCOME_IMAGE = pygame.image.load("assets/welcome.png")
WELCOME_IMAGE = pygame.transform.scale(WELCOME_IMAGE, (150, 150))

WALL_IMAGE = pygame.image.load("assets/mur.png")
WALL_IMAGE = pygame.transform.scale(WALL_IMAGE, (SIZE_SPRITE, SIZE_SPRITE))

PATH_IMAGE = pygame.image.load("assets/fond.jpg")
PATH_IMAGE = pygame.transform.scale(PATH_IMAGE, (SIZE_SPRITE, SIZE_SPRITE))

MCGIVER_IMAGE = pygame.image.load("assets/scientist.png")
MCGIVER_IMAGE = pygame.transform.scale(MCGIVER_IMAGE, (SIZE_SPRITE, SIZE_SPRITE))

GUARD_IMAGE = pygame.image.load("assets/keeper.png")
GUARD_IMAGE = pygame.transform.scale(GUARD_IMAGE, (SIZE_SPRITE, SIZE_SPRITE))

EXIT_IMAGE = pygame.image.load("assets/exit.png")
EXIT_IMAGE = pygame.transform.scale(EXIT_IMAGE, (SIZE_SPRITE, SIZE_SPRITE))

FLASK_1 = pygame.image.load("assets/flask.png")
FLASK_1 = pygame.transform.scale(FLASK_1, (SIZE_SPRITE, SIZE_SPRITE))

FLASK_2 = pygame.image.load("assets/flask2.png")
FLASK_2 = pygame.transform.scale(FLASK_2, (45, 45))

FLASK_3 = pygame.image.load("assets/flask3.png")
FLASK_3 = pygame.transform.scale(FLASK_3, (45, 45))

"""
button properties
"""
BUTTON_X = 120
BUTTON_Y = 400


DICTIONNARY_IMAGE = {
    WALL: WALL_IMAGE,
    PATH: PATH_IMAGE,
    GUARD: GUARD_IMAGE,
    OBJECT_1: FLASK_1,
    OBJECT_2: FLASK_2,
    OBJECT_3: FLASK_1,
    MCGIVER: MCGIVER_IMAGE,
    EXIT: EXIT_IMAGE
}

TITLE = pygame.display.set_caption("Labyrinthe")
