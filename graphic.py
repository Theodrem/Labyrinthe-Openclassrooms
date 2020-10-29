from config import *
from maze import Maze
import pygame


def flip():
    """
    refresh page
    """
    pygame.display.flip()


class Graphic:
    """
    Graphic elements of the game with pygame,
    homepage, maze, object counter,
    """
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH_WINDOWS, HEIGHT_WINDOWS))
        self.icon = pygame.display.set_icon(FLASK_1)
        self.play_button_rect = HOMEPAGE_BUTTON.get_rect()
        self.play_button_rect.x = BUTTON_X
        self.play_button_rect.y = BUTTON_Y
        self.maze = Maze()

    def print(self, text, x, y):
        """
        display object counter
        :param text: text
        :param x: position x
        :param y: position y

        """
        arial_font = pygame.font.SysFont("arial", 80)
        blank = (255, 255, 255)
        text = arial_font.render(str(text), True, blank)
        self.window.blit(text, [x, y])

    def homepage(self, image):
        """
        home page display, play button, welcome_image or win_image or game_over image
        """
        self.window.blit(HOMEPAGE, (0, 0))
        self.window.blit(HOMEPAGE_BANNER, (200, 200))
        self.window.blit(image, (280, 50))
        self.window.blit(HOMEPAGE_BUTTON, self.play_button_rect)

    def display_maze(self):
        """
        for each character in structure display the corresponding image
        """
        for row in self.maze.structure:
            for character in row:
                if character != "\n":
                    self.window.blit((DICTIONNARY_IMAGE[character]), (self.maze.x, self.maze.y))
                self.maze.x += SIZE_SPRITE
            else:
                if self.maze.y <= HEIGHT_WINDOWS:
                    self.maze.x = 0
                    self.maze.y += SIZE_SPRITE
                else:
                    self.maze.y = 0
                    self.maze.x = 0
