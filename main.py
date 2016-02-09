import random

import ImageHandler
from LedCube import LedCube
import math
import numpy


def blinking_edges():
    def is_edge(p):
        return p.count(0) >= 2 or p.count(led_cube.x_count - 1) >= 2 or (0 in p and led_cube.x_count - 1 in p)

    s = 0.01
    color = (1, 0, 0)
    blank_color = (0, 0, 0)

    led_cube.fill_frame(blank_color)
    while True:
        new_frame = []

        for i in range(led_cube.get_led_count()):
            pos = led_cube.get_coords(i)
            if is_edge(pos):
                new_frame.append(color)
            else:
                new_frame.append(None)

        led_cube.update_frame(new_frame)
        led_cube.sleep(s)


def expanding_sphere():
    r = 0
    max_r = led_cube.x_count
    expanding_rate = 1
    d = 2
    s = 0.01
    offset = tuple(numpy.divide((led_cube.x_count, led_cube.y_count, led_cube.z_count), (2, 2, 2)))
    while True:
        led_frame = []
        for i in range(led_cube.get_led_count()):
            pos = tuple(numpy.subtract(led_cube.get_coords(i), offset))
            distance = math.sqrt(sum(map(lambda x: math.pow(x, 2), pos)))
            if r > distance > (r - d):
                led_frame.append((0.8, float(r) / max_r, 0))
            else:
                led_frame.append((0.1, 0.1, 0.1))
        if r < max_r:
            r += expanding_rate
        else:
            r = 0

        led_cube.update_frame(led_frame)
        led_cube.sleep(s)


def sparkles():
    #unfinished
    base_color = (0, 0, 0)
    led_frame = [base_color] * led_cube.get_led_count()
    s = 0.01
    while (True):
        for i in range(led_cube.get_led_count()):
            cur_led = numpy.subtract(led_frame[i], (0.1, 0.1, 0.1))

            if led_frame[i-1] != base_color:
                decay = tuple(1.0 / random.randint(3,5) for i in range(3))
                cur_led = numpy.add(cur_led, numpy.multiply(led_frame[i-1], decay))

            cur_led = tuple(min(max(c, 0), 1) for c in cur_led)
            led_frame[i] = cur_led

        for i in range(led_cube.get_led_count()):
            rand = random.randint(0, 1000)
            if rand == 1000:
                led_frame[i] = (1, 1, 1)
            elif rand == 0:
                led_frame[i] = base_color

        led_cube.update_frame(led_frame)
        led_cube.sleep(s)

def lanes():
    base_color = (0, 0, 0)
    led_frame = [base_color] * led_cube.get_led_count()
    s = 0.001
    while (True):
        for i in range(led_cube.get_led_count(), 0, -1):
            cur_led = led_frame[i]
            prev_led =led_frame[i - 1]
            if i > 0 and prev_led != base_color:
                cur_led = prev_led
            led_frame[i] = cur_led

        # randomly generate new lanes on one side of the cube
        for i in range(led_cube.x_count * led_cube.y_count):
            rand = random.randint(0, 100)
            if rand == 100:
                led_frame[i] = (1, 1, 1)

        led_cube.update_frame(led_frame)
        led_cube.sleep(s)


led_cube = LedCube()

# blinking_edges()
# expanding_sphere()
# ImageHandler.display_image(led_cube, 'invader.bmp')
# sparkles()
lanes()