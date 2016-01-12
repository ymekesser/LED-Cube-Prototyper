from __future__ import division
from random import randint
from visual import sleep, color
from LedCube import LedCube

# Parameters
sleepy_time = 0.03
ITERATIONS = 50 #how many times do we iterate the algo?

led_cube = LedCube()

# Algorithms
# i is the the position of the led (0-512)
def insideOut(i):
    (x, y, z) = led_cube.get_coords(i)
    distance = randint(0,255)
    if x < distance % 9:
        return (i, (x, y, z), color.red, 1.0)
    elif y < distance % 9:
        return (i, (x, y, z), color.blue, 1.0)
    elif z < distance % 9:
        return (i, (x, y, z), color.green, 1.0)
    else:
        return (i, (x, y, z), (0.1,0.1,0.1), 1.0)

def randomAlgo(i):
    (x, y, z) = led_cube.get_coords(i)
    distance = randint(0,255)
    if distance < 20:
        return (i, (x, y, z), color.red, 1.0)
    else:
        return (i, (x, y, z), (0.1,0.1,0.1), 1.0)

# def updateNeopixelStrip(strip, leds):
#     strip = neopixelstrip
#     for idx, led in leds:
#         color = Color(led.color.x * 255.0, led.color.y * 255.0, led.color.z * 255.0)
#         strip.setPixelColor(idx, color)

def setLedPixelColor(led, color, brightness):
    led.color = color
    led.opacity = brightness

# transform scalar int to coordinates, at moment not needed, but possibly helpful



# apply
def apply(fun, *arg):
    return fun(*arg)

# pass an algorithm (Int -> Frame) and an Integer how many frames there are.
# type Color = (Double, Double, Double)
# type Position = (Int, Int, Int)
# type LEDIndex = Brightness = Int
# type Frame = (LEDIndex, Position, Color, Brightness)
def runAlgo(algo, frameCounter):
    animation = []
    for i in range(frameCounter):
        animation.append([apply(algo, i) for i in range(led_cube.x_count * led_cube.y_count * led_cube.z_count)])
    return animation

def animateFrame(leds, frame):
    for l, (i,pos,c,_) in zip(leds, frame):
        setLedPixelColor(l, c, 1.0)
    sleep(sleepy_time)

def runAnimation(leds, animation):
    map(lambda frame: animateFrame(leds, frame), animation)

while (True):
    animation = runAlgo(insideOut, ITERATIONS)
    runAnimation(led_cube.leds, animation)
    animation = runAlgo(randomAlgo, ITERATIONS)
    runAnimation(led_cube.leds, animation)
    print 'animation done.'
