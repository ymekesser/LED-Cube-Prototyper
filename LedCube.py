from __future__ import division
from VisualLedCube import VisualLedCube


class LedCube(object):
    x_count = y_count = z_count = 8
    leds = []

    visual_led_cube = None

    def __init__(self, x_count=None, y_count=None, z_count=None):
        """ Initialize the LED Cube.

        Args:
            x_count (int): The amount of LEDs on the x-axis (width)
            y_count (int): The amount of LEDs on the y-axis (height)
            z_count (int): The amount of LEDs on the z-axis (depth)
        """

        if x_count is not None:
            self.x_count = x_count
        if y_count is not None:
            self.y_count = y_count
        if z_count is not None:
            self.z_count = z_count

        self.init_visual_led_cube()

    def init_visual_led_cube(self):
        self.visual_led_cube = VisualLedCube(
                x_count=self.x_count,
                y_count=self.y_count,
                z_count=self.z_count)

    def update_frame(self, leds):
        """ Update the LEDs in the cube with new color values

        A color value is a tuple of 3 or 4 floats, where each float is a value between 0 and 1, representing
        the intensity of the primary color:
        (red, green, blue, alpha)
        The alpha value is optional and can be left out.
        If a color is not to be changed in this frame, the list element can be None.

        Examples:
            Pure red: (1, 0, 0)
            Yellow: (1, 1, 0)
            Light gray: (0.7, 0.7, 0.7)
            White and half-transparent: (1, 1, 1, 0.5)

        Args:
            leds (list[tuple]): A list of tuples with color values.
        """

        assert (len(leds) == self.get_led_count())
        self.visual_led_cube.update_frame(leds)

    def fill_frame(self, color):
        """ Sets all LEDs in the cube to one color. See update_frame() for how a color is defined.

        Args:
            color (int, int int): The color to set the cube to.
        """
        frame = [color] * self.get_led_count()
        self.update_frame(frame)

    def get_led_count(self):
        """ Returns the amount of LEDs in the cube """
        return self.x_count * self.y_count * self.z_count

    def get_coords(self, i):
        """ Returns the corresponding coordinates in the cube for the index of an LED

        Args:
            i: the index of the LED in the LED list

        Returns:
            (int, int, int): The (x, y, z) vector/tuple with the position of the LED
        """

        (restW, width) = divmod(i, self.x_count)
        (restH, height) = divmod(restW, self.z_count)
        (_, depth) = divmod(restH, self.y_count)
        return (width, height, depth)

    def sleep(self, sleepytime):
        """ Sleep for the specified amount of time.

        Args:
            sleepytime (int): the amount of seconds to sleep
        """
        self.visual_led_cube.sleep(sleepytime)
