# coding: utf8
from personnage import Perso
from config import *
from labyrinthe import Labyrinthe


class GameStart:
    def __init__(self):
        self.lab1 = 0

    def jeu(self):
        maze1 = Labyrinthe("prison.txt")
        maze1.build()
        maze1.display()
        perso1 = Perso(maze1)
        continue_game = True

        while continue_game:
            touch = input()

            if touch == low:
                perso1.move(low)

            elif touch == (high):
                perso1.move(high)

            elif touch == (right):
                perso1.move(right)

            elif touch == (left):
                perso1.move(left)

            elif touch == (inventoryButton):
                perso1.move(inventoryButton)

            else:
                pass

            if perso1.win == False:
                continue_game = False

            maze1.display()
