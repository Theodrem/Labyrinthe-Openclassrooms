# coding: utf8
from player import Player
from config import *
from maze import Maze
import pygame


class GameStart:
    def __init__(self):
        self.init = pygame.init()
        self.is_playing = False
        self.window = pygame.display.set_mode((WIDTH_WINDOWS, HEIGHT_WINDOWS))
        self.icon = pygame.display.set_icon(FLASK_2)
        self.title = TITLE
        self.maze = Maze()
        self.player = Player(self.maze)
        self.x = 0
        self.y = 0
        self.play_button_rect = HOMEPAGE_BUTTON.get_rect()
        self.play_button_rect.x = 160
        self.play_button_rect.y = 470

    def print(self, texte, x, y):
        arial_font = pygame.font.SysFont("arial", 80)
        blank = (255, 255, 255)
        text = arial_font.render(str(texte), True, blank)
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
                    if character == WALL:
                        self.window.blit(WALL_IMAGE, (self.maze.x, self.maze.y))
                    elif character == PATH:
                        self.window.blit(PATH_IMAGE, (self.maze.x, self.maze.y))
                    elif character == MCGIVER:
                        self.window.blit(MCGIVER_IMAGE, (self.maze.x, self.maze.y))
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

    def refresh(self):
        self.is_playing = False
        self.maze.build()
        self.player.x = 1
        self.player.y = 1

    def jeu(self):
        self.maze.build()
        self.homepage(WELCOME_IMAGE)
        continue_game = True

        while continue_game:
            if not self.is_playing:
                self.player.win = False
                self.player.lose = False
            else:
                self.display_maze()
                self.player.respawn()
                self.print(len(self.player.inventory), 0, 0)
                if self.player.win:
                    self.refresh()
                    self.homepage(WIN_IMAGE)

                elif self.player.lose:
                    self.refresh()
                    self.homepage(GAME_OVER_IMAGE)

            pygame.display.flip()

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    continue_game = False
                    quit()

                elif events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_LEFT:
                        self.player.move(LEFT)
                    elif events.key == pygame.K_RIGHT:
                        self.player.move(RIGHT)

                    elif events.key == pygame.K_UP:
                        self.player.move(UP)

                    elif events.key == pygame.K_DOWN:
                        self.player.move(DOWN)

                elif events.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(events.pos):
                        self.is_playing = True








