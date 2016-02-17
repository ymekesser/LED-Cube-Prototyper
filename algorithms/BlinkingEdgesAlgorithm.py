from Algorithm import Algorithm

class BlinkingEdgesAlgorithm(Algorithm):

    def __init__(self, led_cube):
        super(BlinkingEdgesAlgorithm, self).__init__(led_cube)
        self.sleep_time = 0.01
        self.color = (1, 0, 0)

    def is_edge(self, p):
        return p.count(0) >= 2 \
                or p.count(self.led_cube.x_count - 1) >= 2 \
                or (0 in p and self.led_cube.x_count - 1 in p)

    def step(self):
        new_frame = []

        # TODO: should blink
        for i in range(self.led_cube.get_led_count()):
            pos = self.led_cube.get_coords(i)
            if self.is_edge(pos):
                new_frame.append(self.color)
            else:
                new_frame.append(None)

        self.led_cube.update_frame(new_frame)
        self.sleep(self.sleep_time)