import random
import arcade

CRATES: dict[(int, int), any] = {}
ROBOTS = arcade.SpriteList()


def get_active_crates():
    return filter(lambda c: c.activated, CRATES.values())


def random_active_crate():
    return random.choice(list(get_active_crates()))
