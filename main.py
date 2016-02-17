import Controller
from LedCube import LedCube
from visual_common import create_display

# # # # MAIN means start the application --> HERE <-- # # # #

# initialize led_cube and controller
led_cube = LedCube()
Controller.start(led_cube)

# vpython bs
while True:
    # caps the vpython framerate to 60fps
    create_display.rate(60)
