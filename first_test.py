from __future__ import division
from visual import *

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

# Setup
leds = []
offset = vector(xCount, yCount, zCount) / -2 # Offset to center cube
for xPos in range(xCount):
    for yPos in range(yCount):
        for zPos in range(zCount):
            pos = (vector(xPos, yPos, zPos) + offset) * gap
            color = (xPos / xCount, yPos / yCount, zPos / zCount)
            newLed = sphere(pos=pos, radius=radius, color=color, opacity=opacity, material = material)
            leds.append(newLed)

if wires:
    for xPos in range(xCount):
        for zPos in range(zCount):
            pos = (vector(xPos, 0, zPos) + offset) * gap
            cylinder(pos=pos, axis=(0, (yCount - 1) * gap, 0), radius=wireRadius, color=wireColor, material = wireMaterial)

# Algorithms
while(True):
    for led in leds:
        led.color = (1, 0, 0)
        sleep(0.05)