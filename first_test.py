from __future__ import division
from visual import *
import math
import time
from random import randint

# Parameters
gap = 12
xCount = yCount = zCount = 8
radius = 2
opacity = 1
material = materials.emissive

wires = True
wireRadius = 0.1
wireColor = color.gray(0.1)
wireMaterial = materials.plastic

WIDTH = 8
HEIGHT = 8
DEPTH = 8
red = (1,0,0)
green = (0,1,0)
blue = (0,0,1)
s = 0.03
ITERATIONS = 50 #how many times do we iterate the algo?
leds = []

# Setup
def setup():
    offset = vector(xCount, yCount, zCount) / -2  # Offset to center cube
    for xPos in range(xCount):
        for yPos in range(yCount):
            for zPos in range(zCount):
                pos = (vector(xPos, yPos, zPos) + offset) * gap
                color = (xPos / xCount, yPos / yCount, zPos / zCount)
                newLed = sphere(pos=pos, radius=radius, color=color, opacity=opacity, material=material)
                leds.append(newLed)

    if wires:
        for xPos in range(xCount):
            for zPos in range(zCount):
                pos = (vector(xPos, 0, zPos) + offset) * gap
                cylinder(pos=pos, axis=(0, (yCount - 1) * gap, 0), radius=wireRadius, color=wireColor,
                         material=wireMaterial)

# Algorithms
# i is the the position of the led (0-512)
def insideOut(i):
    (x, y, z) = getCoords(i)
    distance = randint(0,255)
    if x < distance % 9:
        return (i, (x, y, z), red, 1.0)
    elif y < distance % 9:
        return (i, (x, y, z), blue, 1.0)
    elif z < distance % 9:
        return (i, (x, y, z), green, 1.0)
    else:
        return (i, (x, y, z), (0.1,0.1,0.1), 1.0)

def randomAlgo(i):
    (x, y, z) = getCoords(i)
    distance = randint(0,255)
    if distance < 20:
        return (i, (x, y, z), red, 1.0)
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
def getCoords(i):
    (restW, width) = divmod(i, WIDTH)
    (restH, height) = divmod(restW, HEIGHT)
    (_, depth) = divmod(restH, DEPTH)
    return (width, height, depth)


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
        animation.append([apply(algo, i) for i in range(WIDTH * HEIGHT * DEPTH)])
    return animation

def animateFrame(leds, frame):
    for l, (i,pos,c,_) in zip(leds, frame):
        setLedPixelColor(l, c, 1.0)
    time.sleep(s)

def runAnimation(leds, animation):
    map(lambda frame: animateFrame(leds, frame), animation)

setup()
while (True):
    animation = runAlgo(insideOut, ITERATIONS)
    runAnimation(leds, animation)
    animation = runAlgo(randomAlgo, ITERATIONS)
    runAnimation(leds, animation)
    print 'animation done.'
