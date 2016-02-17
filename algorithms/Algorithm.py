from abc import ABCMeta, abstractmethod
import thread
import threading
import time
import Log


class Algorithm:
    __metaclass__ = ABCMeta
    RUNNING = 1
    NOT_RUNNING = 0

    def __init__(self, led_cube):
        """ Constructor for an Algorithm.
        MUST be called in init of all inheriting classes.

        Args:
            led_cube (LedCube.LedCube): Reference to the LedCube the agorithms should run on.
        """
        self.led_cube = led_cube
        self.state = Algorithm.NOT_RUNNING
        self.callback = None

    @abstractmethod
    def step(self):
        """
        This method gets called repeatedly while the algorithm is running.

        Put your logic into THIS method.
        Don't forget to sleep (use self.sleep()) at the end of this method or else it
        may run haywire.
        """
        pass

    def __run__(self):
        name = type(self).__name__
        Log.log("Starting [" + name + "]")
        while self.state == Algorithm.RUNNING:
            self.step()
        Log.log("Exiting [" + name + "]")
        if self.callback:
            self.callback()

    def start(self, duration=None, callback=None):
        """ Start this algorithm. It will run in its own thread.

        Args:
            duration (float): if provided, the algorithm will stop itself after this amount of seconds.
            callback (function): gets called after the algorithm stops running.
        """
        self.callback = callback
        self.led_cube.fill_frame((0, 0, 0))
        self.state = Algorithm.RUNNING
        thread.start_new_thread(self.__run__, ())
        if duration:
            threading.Timer(duration, lambda: self.stop()).start()

    def stop(self):
        """ Stop this algorithm.

        The current step will be completed and the callback function, if provided, gets called.

        """
        self.state = Algorithm.NOT_RUNNING

    def sleep(self, sleepytime):
        """ Pause this algorithm for a set amount of seconds.
        Args:
            sleepytime (float): The amount of seconds to sleep.
        """
        time.sleep(sleepytime)

    def is_running(self):
        """ Returns: wether the algorithm is currently running. """
        return self.state == Algorithm.RUNNING
