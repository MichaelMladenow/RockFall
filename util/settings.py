"""
    Utility module to contain the static game settings
"""

SETTINGS = {
    "game_speed": 0.1,               # Duration of intevals between field update (lower = faster)
    "field_rows": 25,                # Field size: Height
    "field_cols": 50,                # Field size: Width
    "tick_rock_move_rows": 1,        # How many rows does each rock move on game loop tick
    "tick_rock_move_cols": 0,        # How many rows does each rock move on game loop tick
    "tick_rock_spawn_rows": [0,1,2], # Which field rows can spawn a rock
}
