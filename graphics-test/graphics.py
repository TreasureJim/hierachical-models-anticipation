import arcade
import timeit
import globals
import state_manager


class GuiScreen(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.draw_time = 1

        self.crate_list = arcade.SpriteList()
        self.zone_list = arcade.ShapeElementList()

    def setup(self):
        self.zone_list.append(
            arcade.create_rectangle_filled(
                globals.MAXIMUM_GRID_X / 2 * globals.GRID_RATIO_X,
                globals.MAXIMUM_GRID_Y / 2 * globals.GRID_RATIO_Y,
                5 * globals.GRID_RATIO_X,
                5 * globals.GRID_RATIO_Y,
                arcade.color.RED,
            )
        )
        # Add areas underneath the boxes
        for y in range(0, globals.MAXIMUM_GRID_Y, 3):
            for x in range(0, globals.MAXIMUM_GRID_Y, 3):
                if (
                    x > globals.MAXIMUM_GRID_X / 2 - 4
                    and x < globals.MAXIMUM_GRID_X / 2 + 2
                    and y > globals.MAXIMUM_GRID_Y / 2 - 4
                    and y < globals.MAXIMUM_GRID_Y / 2 + 2
                ):
                    continue

                self.zone_list.append(
                    arcade.create_rectangle_filled(
                        x * globals.GRID_RATIO_X + globals.GRID_RATIO_X * 1.5,
                        y * globals.GRID_RATIO_Y + globals.GRID_RATIO_X * 1.5,
                        globals.GRID_RATIO_X * 2,
                        globals.GRID_RATIO_Y * 2,
                        arcade.color.COOL_GREY,
                    )
                )

    def update(self, delta_time: float):
        for robot in state_manager.ROBOTS:
            robot.update()

        return super().update(delta_time)

    def on_draw(self):
        self.clear()
        draw_start_time = timeit.default_timer()

        # filter only active crates
        # This is a VERY slow way of drawing these
        # TODO: change this to only add and pop crates WHEN they are picked up or spawned again (managed with a dictionary)
        self.crate_list.clear()
        for crate in state_manager.get_active_crates():
            self.crate_list.append(crate)

        self.zone_list.draw()
        self.crate_list.draw()
        state_manager.ROBOTS.draw()

        for robot in state_manager.ROBOTS:
            if robot.crate.activated:
                draw_x(robot.crate.grid_position)

        # Display fps counter
        output = f"Drawing time: {(1 / self.draw_time):.3f} fps."
        # arcade.draw_text(output, 20, globals.SCREEN_HEIGHT - 40, arcade.color.WHITE, 18)
        self.draw_time = timeit.default_timer() - draw_start_time


def draw_x(position):
    point_list = (
        (
            position[0] * globals.GRID_RATIO_X - globals.GRID_RATIO_X * 0.4,
            position[1] * globals.GRID_RATIO_Y - globals.GRID_RATIO_Y * 0.4,
        ),
        (
            position[0] * globals.GRID_RATIO_X + globals.GRID_RATIO_X * 0.4,
            position[1] * globals.GRID_RATIO_Y + globals.GRID_RATIO_Y * 0.4,
        ),
        (
            position[0] * globals.GRID_RATIO_X - globals.GRID_RATIO_X * 0.4,
            position[1] * globals.GRID_RATIO_Y + globals.GRID_RATIO_Y * 0.4,
        ),
        (
            position[0] * globals.GRID_RATIO_X + globals.GRID_RATIO_X * 0.4,
            position[1] * globals.GRID_RATIO_Y - globals.GRID_RATIO_Y * 0.4,
        ),
    )
    arcade.draw_lines(point_list, arcade.color.RED_DEVIL, 4)


def start():
    screen = GuiScreen(
        globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, globals.SCREEN_TITLE
    )
    screen.setup()
    arcade.run()