# coding: utf8
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
message
"""

WALL_MESSAGE = "Attention au mur!"
SLEEP = "Bravo! Vous avez endormi le garde. Courez vers la sortie pour gagner!"

LOOSE = "Perdu! Vous n'avez pas ramassé tout les objets"
WINNER = "Bravo! Vous avez terminé le labyrinthe."

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
WIDTH_WINDOWS = 675
HEIGHT_WINDOWS = 675

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
WALL_IMAGE = pygame.transform.scale(WALL_IMAGE, (45, 45))

PATH_IMAGE = pygame.image.load("assets/fond.jpg")
PATH_IMAGE = pygame.transform.scale(PATH_IMAGE, (45, 45))

MCGIVER_IMAGE = pygame.image.load("assets/scientist.png")
MCGIVER_IMAGE = pygame.transform.scale(MCGIVER_IMAGE, (45, 45))

GUARD_IMAGE = pygame.image.load("assets/keeper.png")
GUARD_IMAGE = pygame.transform.scale(GUARD_IMAGE, (45, 45))

EXIT_IMAGE = pygame.image.load("assets/exit.png")
EXIT_IMAGE = pygame.transform.scale(EXIT_IMAGE, (45, 45))

FLASK_1 = pygame.image.load("assets/flask.png")
FLASK_1 = pygame.transform.scale(FLASK_1, (45, 45))

FLASK_2 = pygame.image.load("assets/flask2.png")
FLASK_2 = pygame.transform.scale(FLASK_2, (45, 45))

FLASK_3 = pygame.image.load("assets/flask3.png")
FLASK_3 = pygame.transform.scale(FLASK_3, (45, 45))

"""HOMEPAGE = pygame.image.load("assets/fond.jpg")


HOMEPAGE_BANNER = "assets/scientist.png"
HOMEPAGE_BUTTON = "assets/button.png"
GAME_OVER_IMAGE = "assets/game_over.png"
WIN_IMAGE = "assets/win.png"
WELCOME_IMAGE = "assets/welcome.png"
WALL_IMAGE = "assets/mur.png"
PATH_IMAGE = "assets/fond.jpg"
MCGIVER_IMAGE= "assets/scientist.png"
GUARD_IMAGE = "assets/keeper.png"
EXIT_IMAGE = "assets/exit.png"
FLASK_1 = "assets/flask.png"
FLASK_2 = "assets/flask2.png"
FLASK_3 = "assets/flask3.png"
"""

BUTTON_X = 160
BUTTON_Y = 470

DICTIONNARY = {
    WALL: WALL_IMAGE,
    PATH: PATH_IMAGE,
    GUARD: GUARD_IMAGE,
    OBJECT_1: FLASK_1,
    OBJECT_2: FLASK_2,
    OBJECT_3: FLASK_3,
    MCGIVER: MCGIVER_IMAGE,
    EXIT: EXIT_IMAGE
}  # dictionnary with characters and images

"""
pygame title
"""
TITLE = pygame.display.set_caption("Labyrinthe")
