# coding: utf8
from player import Player
from config import *
from graphic import Graphic


class GameStart:
    def __init__(self):
        self.is_playing = False
        self.graphic = Graphic()
        self.player = Player(self.graphic.maze)
        self.continue_game = True

    def refresh(self):
        self.is_playing = False
        self.graphic.maze.build()
        self.player.x = 1
        self.player.y = 1

    def start(self):
        self.graphic.maze.build()
        self.graphic.homepage(WELCOME_IMAGE)

    def not_playing(self):
        self.player.win = False
        self.player.lose = False

    def playing(self):
        self.graphic.display_maze()
        self.player.spawn()
        self.graphic.print(len(self.player.inventory), 0, 0)
        if self.player.win:
            self.refresh()
            self.graphic.homepage(WIN_IMAGE)

        elif self.player.lose:
            self.refresh()
            self.graphic.homepage(GAME_OVER_IMAGE)

    def action(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.continue_game = False
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
                if self.graphic.play_button_rect.collidepoint(events.pos):
                    self.is_playing = True

    def loop(self):
        self.start()
        while self.continue_game:
            if not self.is_playing:
                self.not_playing()
            else:
                self.playing()
            self.graphic.flip()
            self.action()










