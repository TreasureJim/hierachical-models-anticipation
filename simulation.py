import random
import crate
import globals
import robot
import state_manager
import simpy

ENVIRONMENT = simpy.Environment()


def setup():
    # Create all of the crates and randomly make some activated
    for y in range(0, globals.CRATE_GRID_SIZE):
        if y % 3 == 0:
            continue
        for x in range(0, globals.CRATE_GRID_SIZE):
            if (
                x % 3 == 0
                or y > globals.MAXIMUM_GRID_Y / 2 - 3
                and y < globals.MAXIMUM_GRID_Y / 2 + 3
                and x > globals.MAXIMUM_GRID_X / 2 - 3
                and x < globals.MAXIMUM_GRID_X / 2 + 3
            ):
                continue

            activated = bool(random.getrandbits(1))
            state_manager.CRATES[(x, y)] = crate.Crate((x, y), activated)

    # Randomly spawn in robots
    # TODO: Handle if they spawn on top of each other
    for _ in range(globals.NUM_ROBOTS):
        position = (
            random.randrange(1, globals.MAXIMUM_GRID_X / 3) * 3,
            random.randrange(1, globals.MAXIMUM_GRID_X / 3) * 3,
        )
        state_manager.ROBOTS.append(robot.Robot(ENVIRONMENT, position))
