
#!/usr/bin/env python3

#==== MISC MODULES ==========================
import random

#==== GAME MODULES ==========================
from .objects import *
from util import util
from util.settings import SETTINGS



class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._generate_field()

    def _generate_field(self):
        self.field = []
        for row in range(self.height):
            # When generating the field all the cells are filled with empty objects
            self.field.append([EmptyObject(row,col) for col in range(self.width)])

    def get_matrix(self):
        return self.field

    def print_field(self):
        for row in self.get_matrix():
            util.addstr("".join([str(col) for col in row]))
            util.addstr("\r\n")

    def get_cell(self, row, col):
        return self.get_matrix()[row][col]

    def get_empty_objects(self):
        """ Return all the empty cells from the field """
        empty_objects = []
        for row in self.get_matrix():
            for item in row:
                if item.empty:
                    empty_objects.append(item)
        return empty_objects

    def get_nonempty_objects(self):
        """ Returns all the non-empty objects from the field"""
        nonempty_objects = []
        for row in self.get_matrix():
            for item in row:
                if not item.empty:
                    nonempty_objects.append(item)
        return nonempty_objects
        
    def get_random_empty(self):
        """ Returns a random empty field from the field """
        return random.choice(self.get_empty_objects())
        
    

    def place_item(self,item):
        row = item.row
        col = item.col
        cell = self.get_cell(row, col)
        if not cell.empty:
            raise Exception("Cell %s is not empty." % cell.position_string())
        self.field[row][col] = item


    def remove_item(self,row,col):
        cell = self.get_cell(row, col)
        if cell.empty:
            raise Exception("Cell %s is already empty." % cell.position_string())
        self.field[row][col] = EmptyObject(row,col)

    def move_item(self, item, row, col):
        # We check whether the target position is available
        target_row = item.row + row
        target_col = item.col + col

        # TODO: Check matrix boundaries
        if (target_row < 0):
            item.hit_wall("top")
            self.remove_item(item.row, item.col)
        elif (target_row >= self.height):
            item.hit_wall("bottom")
            self.remove_item(item.row, item.col)
        elif (target_col < 0):
            item.hit_wall("left")
            self.remove_item(item.row, item.col)
        elif (target_col >= self.width):
            item.hit_wall("right")
            self.remove_item(item.row, item.col)
        else:
            #print("Current row: %s/%s" % (target_row+1, self.height))
            #print("Current col: %s/%s" % (target_col+1, self.width))
            target_cell = self.get_cell(target_row, target_col)

            if target_cell.player:
                # After moving the object will collide with the player
                target_cell.collide(item)
            elif not target_cell.empty:
                # After moving the target will collide with another object
                target_cell.collide(item)
            else:
                # After moving the target will not collide with anything
                self.place_item(item.move(target_row,target_col))           # Handle the movement
                self.remove_item(target_row - row, target_col - col)

    def tick(self):
        # What happens each game update

        # Move all rocks down
        objects_to_update = self.get_nonempty_objects()
        for item in objects_to_update:
            self.move_item(item,SETTINGS["tick_rock_move_rows"],SETTINGS["tick_rock_move_cols"])

        # Generate a new rock
        empty_cell = self.get_random_empty()
        new_rock   = RockObject(empty_cell.row, empty_cell.col, "*")
        self.place_item(new_rock)