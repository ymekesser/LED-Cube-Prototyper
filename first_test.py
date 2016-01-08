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
s = 0.03
ITERATIONS = 100 #how many times do we iterate the algo?

# Setup
leds = []
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

# def updateNeopixelStrip(strip, leds):
#     strip = neopixelstrip
#     for idx, led in leds:
#         color = Color(led.color.x * 255.0, led.color.y * 255.0, led.color.z * 255.0)
#         strip.setPixelColor(idx, color)

def setLedPixelColor(led, color, brightness):
    led.color = color
    led.opacity = brightness

def getCoords(i):
    (restW, width) = divmod(i, WIDTH)
    (restH, height) = divmod(restW, HEIGHT)
    (blub, depth) = divmod(restH, DEPTH)
    return (width, height, depth)

def randomAlgo(i, r, d):
    (x, y, z) = getCoords(i)
    distance = randint(0,255)
    if distance < r and distance > (r - d):
        return (i, (x, y, z), red, 1.0)
    else:
        return (i, (x, y, z), (0.1,0.1,0.1), 1.0)

def perform( fun, *arg ):
    return fun( *arg )

def runAlgo(algo, frameCounter):
    r = 0
    d = 15
    animation = []
    for i in range(frameCounter):
        animation.append([perform(algo, i, r, d) for i in range(WIDTH * HEIGHT * DEPTH)])
        if r < xCount * gap:
            r = r + 5
        else:
            r = 0
    return animation

def animateFrame(leds, frame):
    for l, (i,pos,c,_) in zip(leds, frame):
        setLedPixelColor(l, c, 1.0)
    time.sleep(s)

def applyAnimation(leds, animation):
    map(lambda frame: animateFrame(leds, frame), animation)

while (True):
    animation = runAlgo(randomAlgo, ITERATIONS)
    print 'animation done.'
    applyAnimation(leds, animation)
