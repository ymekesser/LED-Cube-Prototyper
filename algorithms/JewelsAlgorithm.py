from __future__ import division
from Algorithm import Algorithm
import math
import numpy


class JewelsAlgorithm(Algorithm):
    class Sphere:
        def __init__(self, pos, radius, color):
            self.pos = pos
            self.radius = radius
            self.color = color

        def is_point_in_shape(self, point):
            difference = numpy.subtract(self.pos, point)
            distance = math.sqrt(sum(map(lambda x: math.pow(x, 2), difference)))
            return distance <= self.radius

    class Cylinder:
        def __init__(self, pos, radius, height, color):
            self.pos = pos
            self.radius = radius
            self.height = height
            self.color = color

        def is_point_in_shape(self, point):
            horizontal_pos = (self.pos[0], self.pos[2])
            horizontal_point = (point[0], point[2])
            difference = numpy.subtract(horizontal_pos, horizontal_point)
            distance = math.sqrt(sum(map(lambda x: math.pow(x, 2), difference)))
            return distance <= self.radius and point[1] >= self.pos[1] and point[1] <= self.pos[1] + self.height

    @staticmethod
    def rotateZShape(shape, pivot, angle):
        distance_from_pivot = numpy.subtract(shape.pos, pivot)
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)

        x = distance_from_pivot[0]
        y = distance_from_pivot[1]
        z = distance_from_pivot[2]
        rotated = (
            x * cos_a - y * sin_a,
            y * cos_a + x * sin_a,
            z
        )

        shape.pos = tuple(numpy.add(rotated, pivot))

    @staticmethod
    def rotateY(shape, pivot, angle):
        from_origin = numpy.subtract(shape.pos, pivot)
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)
        x = from_origin[0]
        y = from_origin[1]
        z = from_origin[2]
        rotated = (
            x * cos_a - z * sin_a,
            y,
            z * cos_a + x * sin_a
        )

        shape.pos = tuple(numpy.add(rotated, pivot))

    def __init__(self, led_cube):
        super(JewelsAlgorithm, self).__init__(led_cube)

        self.base_color = (0.1, 0.1, 0.1)
        color = (1, 0.5, 1)
        self.shapes = [
            JewelsAlgorithm.Sphere(
                ((led_cube.x_count - 1) / 2, 1, (led_cube.z_count - 1) / 2 - 2),
                2.5,
                color),
            JewelsAlgorithm.Sphere(
                ((led_cube.x_count - 1) / 2, 1, (led_cube.z_count - 1) / 2 + 2),
                2.5,
                color
            ),
            JewelsAlgorithm.Sphere(
                ((led_cube.x_count - 1) / 2, 6, (led_cube.z_count - 1) / 2),
                1.5,
                color
            ),
            JewelsAlgorithm.Cylinder(
                ((led_cube.x_count - 1) / 2, 0, (led_cube.z_count - 1) / 2),
                2,
                6,
                (1, 0.5, 1)
            )
        ]

    def step(self):
        new_frame = []

        angle = math.pi / 16
        pivot = (
            (self.led_cube.x_count - 1) / 2,
            (self.led_cube.y_count - 1) / 2,
            (self.led_cube.z_count - 1) / 2,
        )
        for shape in self.shapes:
            JewelsAlgorithm.rotateY(shape, pivot, angle)

        for i in range(self.led_cube.get_led_count()):
            color = self.base_color
            for shape in self.shapes:
                current_pos = self.led_cube.get_coords(i)

                if shape.is_point_in_shape(current_pos):
                    color = shape.color
            new_frame.append(color)

        self.led_cube.update_frame(new_frame)
        self.sleep(0.1)
