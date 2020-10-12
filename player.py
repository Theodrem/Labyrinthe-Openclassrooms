# coding: utf8
from config import *


class Player:
    def __init__(self, maze):
        self.x = 1
        self.y = 1
        self.maze = maze
        self.win = False
        self.lose = False
        self.inventory = []
        self.size_inventory = len(self.inventory)

    def spawn(self):
        self.change_position(MCGIVER)

    def attributes(self):
        self.get_objects()
        self.fight_guard()
        self.win_condition()
        self.change_position(MCGIVER)

    def get_position(self):
        return self.maze.structure[self.x][self.y]

    def change_position(self, character):
        self.maze.structure[self.x][self.y] = character

    def move(self, direction):
        if direction == DOWN:
            if self.maze.structure[self.x + 1][self.y] != WALL:
                self.change_position(PATH)
                self.x += 1
                self.attributes()

        elif direction == UP:
            if self.maze.structure[self.x - 1][self.y] != WALL:
                self.change_position(PATH)
                self.x -= 1
                self.attributes()

        elif direction == RIGHT:
            if self.maze.structure[self.x][self.y + 1] != WALL:
                self.change_position(PATH)
                self.y += 1
                self.attributes()

        elif direction == LEFT:
            if self.maze.structure[self.x][self.y - 1] != WALL:
                self.change_position(PATH)
                self.y -= 1
                self.attributes()

    def get_objects(self):
        if self.get_position() in OBJECTS:
            self.inventory.append(self.get_position())

    def fight_guard(self):
        if self.get_position() == GUARD:
            if self.size_inventory == 3:
                self.change_position(PATH)
            else:
                #lose
                self.lose_condition()

    def win_condition(self):
        if self.get_position() == EXIT:
            if GUARD not in self.maze.structure:
                self.win = True
                self.inventory.clear()

    def lose_condition(self):
        self.lose = True
        self.inventory.clear()
