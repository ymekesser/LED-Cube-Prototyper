from __future__ import division
from Algorithm import Algorithm
import numpy
import math
import time

class ExpandingSphereAlgorithm(Algorithm):

    def __init__(self, led_cube):
        super(ExpandingSphereAlgorithm, self).__init__(led_cube)
        self.radius = 0.
        self.max_radius = led_cube.x_count
        self.expanding_rate = 1
        self.thickness = 2
        self.sleep_time = 0.1
        self.center_offset = tuple(\
                numpy.divide((led_cube.x_count-0.5, led_cube.y_count-0.5, led_cube.z_count-0.5), 2))

    def step(self):
        led_frame = []
        for i in range(self.led_cube.get_led_count()):
            pos = tuple(numpy.subtract(self.led_cube.get_coords(i), self.center_offset))
            distance = math.sqrt(sum(map(lambda x: math.pow(x, 2), pos)))
            if self.radius > distance > (self.radius - self.thickness):
                led_frame.append((0.8, self.radius / self.max_radius, 0))
            else:
                led_frame.append((0.1, 0.1, 0.1))
        if self.radius < self.max_radius:
            self.radius += self.expanding_rate
        else:
            self.radius = 0

        self.led_cube.update_frame(led_frame)
        time.sleep(self.sleep_time)