import time
import thread
from importlib import import_module
from os import path
import inspect
import Log
from algorithms.Algorithm import Algorithm

ALGORITHM_PACKAGE = 'algorithms'


def __visit_algorithms__(arg, dirname, names):
    for filename in names:
        name, ext = path.splitext(filename)
        if ext == '.py' and name not in ('__init__', 'Algorithm'):
            arg.update([name])


def get_algorithm_classes(package=ALGORITHM_PACKAGE):
    """ Read all classes located in the algorithm package.

    Assumes there is a package directory on workdir level, containing ONLY modules with classes in them, which inherit
    from the abstract class Algorithm. There can be multiple classes per module. Nested packages are not possible atm.

    Args:
        package (str): the name of the algorithm package.

    Returns (List): a list of classes.
    """

    algorithm_names = set()
    if path.isdir(package):
        path.walk(package, __visit_algorithms__, algorithm_names)

    algorithm_classes = []
    for algorithm_name in algorithm_names:
        algorithm_package_path = package + "." + algorithm_name
        algorithm_module = import_module(algorithm_package_path)
        if inspect.ismodule(algorithm_module):
            for name, obj in inspect.getmembers(algorithm_module):
                if inspect.isclass(obj) and name != 'Algorithm':
                    algorithm_classes.append(obj)
        else:
            Log.log("Module " + algorithm_package_path + " could not be loaded")
    return algorithm_classes


def start(led_cube):
    """ Start controller. It will run in its own little cozy thread.

    Args:
        led_cube (LedCube.LedCube): Reference to the led_cube, this controller should control.
    """
    thread.start_new_thread(__control__, (led_cube,))


def __control__(led_cube):
    """ Actual logic of the controller is in here """
    algorithms = get_algorithm_classes()
    duration = 10

    while True:
        for algorithm in algorithms:
            algorithm_instance = algorithm(led_cube)
            assert (isinstance(algorithm_instance, Algorithm))
            algorithm_instance.start(duration)
            time.sleep(duration)
