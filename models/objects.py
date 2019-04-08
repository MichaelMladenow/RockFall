class GameObject:
    def __init__(self, row, col, symbol, is_empty=True, is_player=False):
        self.row = row
        self.col = col
        self.symbol = symbol
        self.empty = is_empty
        self.player = is_player

    def __str__(self):
        return self.symbol

    def collide(self, collided_object):
        pass

    def hit_wall(self, wall):
        print("%s hit the %s wall." % (str(self), wall))

    def position_string(self):
        return "Left: %d, Right: %d" % (self.row, self.col)

    def move(self,row,col):
        self.row = row
        self.col = col
        return self

class RockObject(GameObject):
    def __init__(self, row, col, symbol):
        return super().__init__(row, col, symbol, is_empty=False, is_player=False)

class EmptyObject(GameObject):
    def __init__(self, row, col, symbol="."):
        return super().__init__(row, col, symbol, is_empty=True, is_player=False)

class PlayerObject(GameObject):
    def __init__(self, row, col, symbol):
        return super().__init__(row, col, symbol, is_empty=True, is_player=True)
