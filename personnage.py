# coding: utf8
from config import *
from labyrinthe import Labyrinthe


class Perso:
    def __init__(self, maze):
        self.x = 1
        self.y = 1
        self.direction = right
        self.maze = maze
        self.win = True
        self.objects = objects
        self.inventory = []

    def move(self, direction):
        lab = Labyrinthe("prison.txt")
        if direction == (low):
            if self.maze.structure[self.x + 1][self.y] == wall:
                print(wall_message)
            elif self.maze.structure[self.x + 1][self.y] != wall:
                self.maze.structure[self.x][self.y] = way
                self.x += 1
                self.get_objects()
                self.win_conditon()
                self.maze.structure[self.x][self.y] = mcgyver

        elif direction == (high):
            if self.maze.structure[self.x - 1][self.y] == wall:
                print(wall_message)
            elif self.maze.structure[self.x - 1][self.y] != wall:
                self.maze.structure[self.x][self.y] = way
                self.x -= 1
                self.get_objects()
                self.win_conditon()
                self.maze.structure[self.x][self.y] = mcgyver

        elif direction == (right):
            if self.maze.structure[self.x][self.y + 1] == wall:
                print(wall_message)
            elif self.maze.structure[self.x][self.y + 1] != wall:
                self.maze.structure[self.x][self.y] = way
                self.y += 1
                self.get_objects()
                self.win_conditon()
                self.maze.structure[self.x][self.y] = mcgyver

        elif direction == (left):
            if self.maze.structure[self.x][self.y - 1] == wall:
                print(wall_message)
            elif self.maze.structure[self.x][self.y - 1] != wall:
                self.maze.structure[self.x][self.y] = way
                self.y -= 1
                self.get_objects()
                self.win_conditon()
                self.maze.structure[self.x][self.y] = mcgyver

        elif direction == (inventoryButton):
            print(len(self.inventory))

    def get_objects(self):
        if self.maze.structure[self.x][self.y] in (self.objects):
            self.inventory.append(self.maze.structure[self.x][self.y])

    def win_conditon(self):
        if self.maze.structure[self.x][self.y] == (guardian):
            if len(self.inventory) == 5:
                print(guardians_sleeping)
            else:
                print(guardian_loose)
                self.win = False

        if self.maze.structure[self.x][self.y] == (exit):
            if guardian not in self.maze.structure:
                print(winner)
                self.win = False
