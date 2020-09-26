# coding: utf8
from player import Player
from config import *
from maze import Maze
import pygame


class GameStart:
    def __init__(self):
        self.init = pygame.init()
        self.window = pygame.display.set_mode((WIDTH_WINDOWS, HEIGHT_WINDOWS))
        self.icon = pygame.display.set_icon(FLASK_2)
        self.title = TITLE
        self.maze = Maze()
        self.player = Player(self.maze)
        self.x = 0
        self.y = 0

    def display_maze(self):
        for row in self.maze.structure:
            for character in row:
                if character != ("\n"):
                    if character == WALL:
                        self.window.blit(WALL_IMAGE, (self.maze.x, self.maze.y))
                    elif character == PATH:
                        self.window.blit(PATH_IMAGE, (self.maze.x, self.maze.y))
                    elif character == MCGIVER:
                        self.window.blit (MCGIVER_IMAGE, (self.maze.x, self.maze.y))
                    elif character == OBJECT_1:
                        self.window.blit(FLASK_1, (self.maze.x, self.maze.y))
                    elif character == OBJECT_2:
                        self.window.blit(FLASK_2, (self.maze.x, self.maze.y))
                    elif character == OBJECT_3:
                        self.window.blit(FLASK_3, (self.maze.x, self.maze.y))
                    elif character == GUARD:
                        self.window.blit(GUARD_IMAGE, (self.maze.x, self.maze.y))
                    elif character == EXIT:
                        self.window.blit(EXIT_IMAGE, (self.maze.x, self.maze.y))
                    self.maze.x += 45
                else:
                    if self.maze.y <= HEIGHT_WINDOWS:
                        self.maze.x = 0
                        self.maze.y += 45
                    else:
                        self.maze.y = 0

    def jeu(self):
        self.maze.build()
        continue_game = True

        while continue_game:

            self.display_maze()
            pygame.display.flip()

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    continue_game = False
                    pygame.quit()

                elif events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_LEFT:
                        self.player.move(LEFT)

                    elif events.key == pygame.K_RIGHT:
                        self.player.move(RIGHT)

                    elif events.key == pygame.K_UP:
                        self.player.move(UP)

                    elif events.key == pygame.K_DOWN:
                        self.player.move(DOWN)

            if self.player.win:
                continue_game = False
                pygame.quit()
            elif self.player.lose:
                continue_game = False
                pygame.quit()






