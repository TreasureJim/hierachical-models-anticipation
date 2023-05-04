import random
import arcade
import globals


class Robot(arcade.Sprite):
    def __init__(self, position):
        super().__init__("sprites/truck.png", 0.08)
        self.grid_position = position

        self.center_x = position[0] * globals.GRID_RATIO_X
        self.center_y = position[1] * globals.GRID_RATIO_Y

        self.pick_crate()

    def pick_crate(self):
        self.crate = globals.CRATES[random.choice(list(globals.CRATES.keys()))]
        print(self.crate)
