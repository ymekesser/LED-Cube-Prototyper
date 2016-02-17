from Algorithm import Algorithm
import ImageHandler
import time

class DisplaySpaceInvaderAlgorithm(Algorithm):

    IMAGE_PATH = 'images/invader.bmp'

    def __init__(self, led_cube):
        super(DisplaySpaceInvaderAlgorithm, self).__init__(led_cube)
        self.image = ImageHandler.load_color_map(self.IMAGE_PATH)

    def step(self):
        ImageHandler.display_image_map(self.led_cube, self.image)
        time.sleep(0.1)