import pygame
from config import *
from maze import Maze


class Graphic:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH_WINDOWS, HEIGHT_WINDOWS))
        self.icon = pygame.display.set_icon(FLASK_1)
        self.play_button_rect = HOMEPAGE_BUTTON.get_rect()
        self.play_button_rect.x = BUTTON_X
        self.play_button_rect.y = BUTTON_Y
        self.maze = Maze()

    def print(self, text, x, y):
        arial_font = pygame.font.SysFont("arial", 80)
        blank = (255, 255, 255)
        text = arial_font.render(str(text), True, blank)
        self.window.blit(text, [x, y])

    def homepage(self, image):
        self.window.blit(HOMEPAGE, (0, 0))
        self.window.blit(HOMEPAGE_BANNER, (200, 200))
        self.window.blit(image, (280, 50))
        self.window.blit(HOMEPAGE_BUTTON, self.play_button_rect)

    def display_maze(self):
        for row in self.maze.structure:
            for character in row:
                if character != ("\n"):
                    self.window.blit((DICTIONNARY[character]), (self.maze.x, self.maze.y))
                self.maze.x += 45
            else:
                if self.maze.y <= HEIGHT_WINDOWS:
                    self.maze.x = 0
                    self.maze.y += 45
                else:
                    self.maze.y = 0
                    self.maze.x = 0

    def flip(self):
        pygame.display.flip()