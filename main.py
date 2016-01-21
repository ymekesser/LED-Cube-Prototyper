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


led_cube = LedCube()

# blinking_edges()
# expanding_sphere()
ImageHandler.display_image(led_cube, 'invader.bmp')
