# coding: utf8
import os
import random
from config import *


class Maze:
    def __init__(self):
        self.structure = []
        self.x = 0
        self.y = 0
        self.object = 0

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

    def display(self):
        for row in self.structure:
            for character in row:
                if character != ("\n"):
                    print(character, end="")
                else:
                    print()

    def object_placing(self):
        number_objects = 0
        while number_objects < 3:
            randomX = random.randint(1, 10)
            randomY = random.randint(1, 10)
            if self.structure[randomX][randomY] == PATH:
                self.structure[randomX][randomY] = OBJECTS[number_objects]
                number_objects += 1