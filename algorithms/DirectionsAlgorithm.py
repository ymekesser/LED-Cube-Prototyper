from __future__ import division
from algorithms.Algorithm import Algorithm
import numpy


class DirectionsAlgorithm(Algorithm):
    def __init__(self, led_cube):
        super(DirectionsAlgorithm, self).__init__(led_cube)
        self.base_color = (0.1, 0.1, 0.1)  # DARK
        self.origin_color = (1, 1, 1)  # WHITE
        self.x_color = (1, 0, 0)  # RED
        self.y_color = (0, 1, 0)  # GREEN
        self.z_color = (0, 0, 1)  # BLUE

        self.frame = []
        for x in range(self.led_cube.x_count):
            for y in range(self.led_cube.y_count):
                for z in range(self.led_cube.z_count):
                    if x == y == z == 0:
                        self.frame.append(self.origin_color)
                    elif y == 0 and z == 0:
                        self.frame.append(self.x_color)
                    elif x == 0 and z == 0:
                        self.frame.append(self.y_color)
                    elif x == 0 and y == 0:
                        self.frame.append(self.z_color)
                    else:
                        self.frame.append(self.base_color)
        self.displayed = False

    def step(self):
        if not self.displayed:
            self.led_cube.update_frame(self.frame)
            self.displayed = True
