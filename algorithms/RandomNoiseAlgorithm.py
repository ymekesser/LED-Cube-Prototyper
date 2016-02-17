from __future__ import division
from algorithms.Algorithm import Algorithm
import random
import numpy

class RandomNoiseAlgorithm(Algorithm):

    def __init__(self, led_cube):
        super(RandomNoiseAlgorithm, self).__init__(led_cube)
        self.primary_color = (1,1,1)
        self.secondary_color = (0,0,0)

    def step(self):
        new_frame = []

        for i in range(self.led_cube.get_led_count()):
            intensity = 1 / random.randint(1, 256)
            noise = numpy.multiply(self.primary_color, intensity)
            color = tuple(numpy.add(self.secondary_color, noise))
            new_frame.append(color)

        self.led_cube.update_frame(new_frame)
        self.sleep(0.1)

class AnotherRandomNoiseAlgorithm(Algorithm):

    def __init__(self, led_cube):
        super(AnotherRandomNoiseAlgorithm, self).__init__(led_cube)
        self.primary_color = (1,1,0)
        self.secondary_color = (0,0.5,0.5)

    def step(self):
        new_frame = []

        for i in range(self.led_cube.get_led_count()):
            intensity = 1 / random.randint(1, 256)
            noise = numpy.multiply(self.primary_color, intensity)
            color = tuple(numpy.add(self.secondary_color, noise))
            new_frame.append(color)

        self.led_cube.update_frame(new_frame)
        self.sleep(0.1)