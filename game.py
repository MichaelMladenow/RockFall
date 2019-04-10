#!/usr/bin/env python3

#==== MISC MODULES ==========================
import _thread, time, msvcrt

#==== GAME MODULES ==========================
from models.objects import *
from models.game_field import GameField
from util import util
from util.settings import SETTINGS



class Game:
    def __init__(self, field_height=SETTINGS["field_rows"], field_width=SETTINGS["field_cols"]):
        self.field = GameField(field_width, field_height)
        self.should_stop = False

        # TODO: Export into a class
        # TODO: Limit inputs in queue to prevent overflow/input lag
        self.input_queue = []

        # Player currently spawns at the middle of the last row
        # TODO: Export spawn position(function of position) into SETTINGS
        self.player = PlayerObject(self.field.height - 1, (self.field.width // 2) - 1, "#")
        self.place_item(self.player)

    def get_field(self):
        return self.field.get_matrix()

    def print_field(self):
        return self.field.print_field()

    def move_item(self,item,row,col):
        self.field.move_item(item,row,col)

    def place_item(self,item):
        return self.field.place_item(item)

    def input_loop(self,thread_name, delay):
        # TODO: Run input loop
        pass

        while not self.should_stop:
            kp = str(msvcrt.getch())
            if kp:
                raise Exception(kp, ord(kp))
                """
                pressed_key = ord(kp)
                if pressed_key == 19424:
                    # Left arrow key
                    # TODO: Move player left
                    print("LEFT!")
                    pass
                elif pressed_key == 19936:
                    # Right arrow key
                    # TODO: Move player right
                    print("RIGHT!")
                    pass
                """
            # TODO: Capture input from the input loop
            # And if there's room add it to the input
            # queue

    def game_loop(self,thread_name, delay):
        while not self.should_stop:
            self.field.tick()
            util.clear_console()
            util.move_cursor(0,0)
            self.print_field()
            time.sleep(delay)

    def start_game(self):
        _thread.start_new_thread(self.game_loop,("GameLoop-Thread", SETTINGS["game_speed"]))
        _thread.start_new_thread(self.input_loop,("InputLoop-Thread", SETTINGS["input_speed"]))
        # TODO: Start input listener thread

if __name__ == "__main__":
    game = Game(SETTINGS["field_rows"], SETTINGS["field_cols"])
    game.start_game()

    # otherwise it just runs and closes :(
    c = input("Type something to quit.")
