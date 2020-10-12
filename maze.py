# coding: utf8
import os
import random
from config import *


class Maze:
    def __init__(self):
        self.structure = []
        self.x = 0
        self.y = 0

    def build(self):
        for filename in os.listdir(DIRECTORY_MAP):
            if filename.endswith(".txt"):
                path = os.path.join(DIRECTORY_MAP, filename)
                with open(path, "r") as file:
                    content = file.readlines()
                    maps = []

                for row in content:
                    line = []
                    for character in row:
                        line.append(character)
                    maps.append(line)

        self.structure = maps
        self.object_placing()

    def object_placing(self):
        number_objects = 0
        while number_objects < 3:
            random_x = random.randint(1, 10)
            random_y = random.randint(1, 10)
            if self.structure[random_x][random_y] == PATH:
                self.structure[random_x][random_y] = OBJECTS[number_objects]
                number_objects += 1