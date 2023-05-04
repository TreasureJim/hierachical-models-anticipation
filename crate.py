import arcade
import random

import globals


class Crate(arcade.Sprite):
    def __init__(self, position, activated):
        super().__init__("./sprites/crate.png", 0.09)
        self.grid_position = position
        self.center_x = position[0] * globals.GRID_RATIO_X
        self.center_y = position[1] * globals.GRID_RATIO_Y

        self.activated = activated
