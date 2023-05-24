import random
import arcade
import globals
import state_manager


class Robot(arcade.Sprite):
    def __init__(self, env, position):
        super().__init__("sprites/truck.png", 0.08)
        self.env = env
        self.grid_position = position

        self.center_x = position[0] * globals.GRID_RATIO_X
        self.center_y = position[1] * globals.GRID_RATIO_Y
        self.crate = state_manager.random_active_crate()

    def pick_crate(self):
        self.crate = globals.CRATES[random.choice(list(globals.CRATES.keys()))]

    def update(self):
        self.change_x = state_manager.ROBOT_SPEED
        return super().update()
