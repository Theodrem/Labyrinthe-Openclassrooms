# coding: utf8
from player import Player
from config import *
from maze import Maze


class GameStart:
    def __init__(self):
        self.lab1 = 0

    def jeu(self):
        maze1 = Maze("prison.txt")
        maze1.build()
        maze1.display()
        player1 = Player(maze1)
        continue_game = True

        while continue_game:
            touch = input()

            if touch == LOW:
                player1.move(LOW)

            elif touch == (HIGH):
                player1.move(HIGH)

            elif touch == (RIGHT):
                player1.move(RIGHT)

            elif touch == (LEFT):
                player1.move(LEFT)

            elif touch == (INVENTORY_BUTTON):
                player1.move(INVENTORY_BUTTON)

            else:
                pass

            if player1.win == True:
                continue_game = False

            maze1.display()
