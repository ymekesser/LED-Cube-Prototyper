from __future__ import division
from visual import *
import itertools


class VisualLedCube(object):
    gap = 12
    x_count = y_count = z_count = 8
    radius = 2
    opacity = 1
    material = materials.emissive

    wires = True
    wireRadius = 0.1
    wireColor = color.gray(0.1)
    wireMaterial = materials.plastic

    leds = []
    offset = None

    def __init__(self, gap=None, x_count=None, y_count=None, z_count=None):
        if gap is not None:
            self.gap = gap
        if x_count is not None:
            self.x_count = x_count
        if y_count is not None:
            self.y_count = y_count
        if z_count is not None:
            self.z_count = z_count
        self.reset()

    def reset(self):
        self.offset = vector(self.x_count, self.y_count, self.z_count) / -2  # Offset to center cube
        for xPos in range(self.x_count):
            for yPos in range(self.y_count):
                for zPos in range(self.z_count):
                    pos = (vector(xPos, yPos, zPos) + self.offset) * self.gap
                    color = (
                        xPos / self.x_count,
                        yPos / self.y_count,
                        zPos / self.z_count)
                    newLed = sphere(
                            pos=pos,
                            radius=self.radius,
                            color=color,
                            opacity=self.opacity,
                            material=self.material)
                    self.leds.append(newLed)

        if self.wires:
            for xPos in range(self.x_count):
                for zPos in range(self.z_count):
                    pos = (vector(xPos, 0, zPos) + self.offset) * self.gap
                    cylinder(
                            pos=pos,
                            axis=(0, (self.y_count - 1) * self.gap, 0),
                            radius=self.wireRadius,
                            color=self.wireColor,
                            material=self.wireMaterial)

    def update_frame(self, led_colors):
        assert len(led_colors) == len(self.leds)
        for led, color in itertools.izip(self.leds, led_colors):
            self.set_led_color(led, color)

    def set_led_color(self, led, color):
        if color is not None:
                led.color = color[:3]
                if len(color) > 3:
                    led.opacity = color[3]

    def sleep(self, sleepytime):
        sleep(sleepytime)
