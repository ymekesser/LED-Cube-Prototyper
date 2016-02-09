from LedCube import LedCube
from PIL import Image


def load_color_map(path):
    """ Loads the content of an image file into a 2D map (nested list)

    Only tested with Bitmaps, so far!

    Args:
        path (str): The path to the image file

    Returns:
        List[List[(int, int, int)]]: A List of Image rows, containing rgb-value tuples
    """
    image_map = []
    with Image.open(path) as image:
        size = image.size
        for x in range(size[0]):
            image_line = []
            for y in range(size[1]):
                r, g, b = image.getpixel((x, size[1] - y - 1))
                image_line.append((r / 255., g / 255., b / 255.))
            image_map.append(image_line)
        return image_map


def display_image_map(led_cube, image_map, fade=True):
    """ Displays an ImageMap on the LedCube

    Args:
        led_cube (LedCube): The LedCube instance the image should be displayed on
        image_map (List[List[(int, int, int)]]): A List of Image rows, containing rgb-value tuples
        fade (bool): Optional. Determines wether the image fades out towards the back.
    """
    if len(image_map) != led_cube.x_count or len(image_map[0]) != led_cube.y_count:
        raise Exception('Size mismatch between cube and image dimensions')

    led_frame = []
    for x in range(led_cube.x_count):
        for y in range(led_cube.y_count):
            for z in range(led_cube.z_count):
                r, g, b = image_map[x][y]
                if fade:
                    a = float(z) / led_cube.z_count
                else:
                    a = 1
                led_frame.append((r, g, b, a))
    led_cube.update_frame([(1, 1, 1)] + led_frame[1:])


def display_image(led_cube, path, fade=True):
    """ Displays an Image loaded from the file system on the LedCube

    Args:
        led_cube (LedCube): The LedCube instance the image should be displayed on
        path (str): The filepath, where the image is located
        fade (bool): Optional. Determines wether the image fades out towards the back.
    """
    image_map = load_color_map(path)
    display_image_map(led_cube, image_map, fade)
