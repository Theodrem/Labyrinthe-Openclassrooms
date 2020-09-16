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
        self.objects = OBJECTS
        self.inventory = []

    def move(self, direction):
        lab = Maze("prison.txt")
        if direction == (LOW):
            if self.maze.structure[self.x + 1][self.y] == WALL:
                print(WALL_MESSAGE)
            elif self.maze.structure[self.x + 1][self.y] != WALL:
                self.maze.structure[self.x][self.y] = WAY
                self.x += 1
                self.get_objects()
                self.win_conditon()
                self.maze.structure[self.x][self.y] = MCGIVER

        elif direction == (HIGH):
            if self.maze.structure[self.x - 1][self.y] == WALL:
                print(WALL_MESSAGE)
            elif self.maze.structure[self.x - 1][self.y] != WALL:
                self.maze.structure[self.x][self.y] = WAY
                self.x -= 1
                self.get_objects()
                self.win_conditon()
                self.maze.structure[self.x][self.y] = MCGIVER

        elif direction == (RIGHT):
            if self.maze.structure[self.x][self.y + 1] == WALL:
                print(WALL_MESSAGE)
            elif self.maze.structure[self.x][self.y + 1] != WALL:
                self.maze.structure[self.x][self.y] = WAY
                self.y += 1
                self.get_objects()
                self.win_conditon()
                self.maze.structure[self.x][self.y] = MCGIVER

        elif direction == (LEFT):
            if self.maze.structure[self.x][self.y - 1] == WALL:
                print(WALL_MESSAGE)
            elif self.maze.structure[self.x][self.y - 1] != WALL:
                self.maze.structure[self.x][self.y] = WAY
                self.y -= 1
                self.get_objects()
                self.win_conditon()
                self.maze.structure[self.x][self.y] = MCGIVER

        elif direction == (INVENTORY_BUTTON):
            print(len(self.inventory))

    def get_objects(self):
        if self.maze.structure[self.x][self.y] in (self.objects):
            self.inventory.append(self.maze.structure[self.x][self.y])

    def win_conditon(self):
        if self.maze.structure[self.x][self.y] == (GUARD):
            if len(self.inventory) == 5:
                print(SLEEP)
            else:
                print(LOOSE)
                self.win = True

        if self.maze.structure[self.x][self.y] == (exit):
            if GUARD not in self.maze.structure:
                print(WINNER)
                self.win = True
