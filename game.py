# coding: utf8
from player import Player
from config import *
from graphic import Graphic


class GameStart:
    """
    link between classes: Maze, Player, Graphic
    """
    def __init__(self):
        self.is_playing = False
        self.graphic = Graphic()
        self.player = Player(self.graphic.maze)
        self.continue_game = True
        self.size_inventory = len(self.player.inventory)

    def start(self):
        """
       Start the game, building the maze, placement of the player
        """
        self.is_playing = False
        self.graphic.maze.build()
        self.player.x = 1
        self.player.y = 1

    def not_playing(self):
        """
        On the home page, game at the stop
        """
        self.player.win = False
        self.player.lose = False

    def playing(self):
        """
        dysplay the maze,
        respawn the player,
        display the counter of inventory
        if the player wins or loses the game is restarted, and display on home page won image or game over image
        """
        self.graphic.display_maze()
        self.player.spawn()
        self.graphic.print(len(self.player.inventory), 0, 0)
        if self.player.win:
            self.start()
            self.graphic.homepage(WIN_IMAGE)

        elif self.player.lose:
            self.start()
            self.graphic.homepage(GAME_OVER_IMAGE)

    def action(self):
        """
        detection of keys pressed by the player,
        close button or play button and directional keys
        """
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
        """
        home screen,
        Starting the game,
        loop of the part
        end of the game with victory or defeat
        """
        self.start()
        self.graphic.homepage(WELCOME_IMAGE)
        while self.continue_game:
            if self.is_playing:
                self.playing()
            else:
                self.not_playing()
            self.graphic.flip()
            self.action()










