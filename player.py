from config import *


class Player:
    """
    Attributes of the player, move, win conditions, lose conditions
    """
    def __init__(self, maze):
        self.x = 1
        self.y = 1
        self.maze = maze
        self.win = False
        self.lose = False
        self.inventory = []

    def get_position(self):
        """
        :return postion of the player
        """
        return self.maze.structure[self.x][self.y]

    def change_position(self, character):
        """
        change position of the player
        :param character
        """
        self.maze.structure[self.x][self.y] = character

    def get_objects(self):
        """
        add object in the inventory
        """
        if self.get_position() in OBJECTS:
            self.inventory.append(self.get_position())

    def fight_guard(self):
        """
        if the player has all the items in his inventory he kills the guard else he dies
        """
        if self.get_position() == GUARD:
            if (len(self.inventory)) == 3:
                self.change_position(PATH)
            else:
                self.lose_condition()

    def win_condition(self):
        """
        if the player get at the exit and the guard is dead, the player wins the game,
        empty inventory
        """
        if self.get_position() == EXIT:
            if GUARD not in self.maze.structure:
                self.win = True
                self.inventory.clear()

    def lose_condition(self):
        """
        the player loses,
        empty inventory
        """
        self.lose = True
        self.inventory.clear()

    def attributes(self):
        """
        apply the player's functions
        """
        self.get_objects()
        self.fight_guard()
        self.win_condition()
        self.change_position(MCGIVER)
        
    def move(self, direction):
        """
        :param direction: (down, up, right, left)
        if next position of the player isn't a wall,
        change actual position player with a path,
        verify fight with the guard,
        verify win condition,
        verify lose condition,
        change next position with player,
        """
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
