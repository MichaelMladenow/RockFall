#!/usr/bin/env python3

#==== MISC MODULES ==========================
import _thread, time

#==== GAME MODULES ==========================
from models.objects import *
from models.game_field import GameField
from util import util
from util.settings import SETTINGS



class Game:
    def __init__(self, field_height=25, field_width=50):
        self.field = GameField(field_width, field_height)
        self.should_stop = False

    def get_field(self):
        return self.field.get_matrix()

    def print_field(self):
        return self.field.print_field()

    def move_item(self,item,row,col):
        self.field.move_item(item,row,col)

    def game_loop(self,thread_name, delay):
        while not self.should_stop:
            self.field.tick()
            util.clear_console()
            util.move_cursor(0,0)
            self.print_field()
            time.sleep(delay)

    def start_game(self):
        _thread.start_new_thread(self.game_loop,("GameLoop-Thread", SETTINGS["game_speed"]))
        # TODO: Start input listener thread

if __name__ == "__main__":
    game = Game(SETTINGS["field_rows"], SETTINGS["field_cols"])
    game.start_game()

    # otherwise it just quits :(
    c = input("Type something to quit.")
