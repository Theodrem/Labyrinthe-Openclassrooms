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
FILE_NAME= "prison.txt"
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
OBJECT_3 ="C"
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


"""
pygame title
"""
TITLE = pygame.display.set_caption("Labyrinthe")
