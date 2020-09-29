# coding: utf8
from config import *
from maze import Maze


class Player:
    def __init__(self, maze):
        self.x = 1
        self.y = 1
        self.direction = RIGHT
        self.maze = maze
        self.win = False
        self.lose = False
        self.objects = OBJECTS
        self.inventory = []

    def respawn(self):
        self.maze.structure[self.x][self.y] = MCGIVER

    def attributes(self):
        self.get_objects()
        self.win_condition()
        self.maze.structure[self.x][self.y] = MCGIVER

    def move(self, direction):
        if direction == DOWN:
            if self.maze.structure[self.x + 1][self.y] == WALL:
                print(WALL_MESSAGE)
            elif self.maze.structure[self.x + 1][self.y] != WALL:
                self.maze.structure[self.x][self.y] = PATH
                self.x += 1
                self.attributes()

        elif direction == UP:
            if self.maze.structure[self.x - 1][self.y] == WALL:
                print(WALL_MESSAGE)
            elif self.maze.structure[self.x - 1][self.y] != WALL:
                self.maze.structure[self.x][self.y] = PATH
                self.x -= 1
                self.attributes()

        elif direction == RIGHT:
            if self.maze.structure[self.x][self.y + 1] == WALL:
                print(WALL_MESSAGE)
            elif self.maze.structure[self.x][self.y + 1] != WALL:
                self.maze.structure[self.x][self.y] = PATH
                self.y += 1
                self.attributes()

        elif direction == LEFT:
            if self.maze.structure[self.x][self.y - 1] == WALL:
                print(WALL_MESSAGE)
            elif self.maze.structure[self.x][self.y - 1] != WALL:
                self.maze.structure[self.x][self.y] = PATH
                self.y -= 1
                self.attributes()

    def get_objects(self):
        if self.maze.structure[self.x][self.y] in (self.objects):
            self.inventory.append(self.maze.structure[self.x][self.y])

    def win_condition(self):
        if self.maze.structure[self.x][self.y] == (GUARD):
            if len(self.inventory) == 3:
                self.maze.structure[self.x][self.y] = PATH

            else:
                #lose
                self.lose = True
                self.inventory.clear()
                self.respawn()

        if self.maze.structure[self.x][self.y] == (EXIT):
            if GUARD not in self.maze.structure:
                print(WINNER)
                self.win = True
                self.inventory.clear()
