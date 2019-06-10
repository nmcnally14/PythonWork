"""Computing Madelbrot sets."""

import math

def mandel(real, imag):
    """

    :param real: the real coordinate
    :param imag: the imaginary coordinate
    :return: an integer in the range 1 - 255
    """
    x = 0
    y = 0
    for i in range (1, 257):
        if x * x + y * y > 4.0:
            break
        xt = real + x * x - y * y
        y = imag + 2.0 * x * y
        x = xt
    return int(math.log(i) * 256 / math.log(256)) - 1

def mandelbrot(size_x, size_y):
    """
    :param size_x: image width
    :param size_y: image height
    :return: a list of lists of ints in range of 0 - 255
    """
    return [[mandel((3.5 * x / size_x) - 2.5,
                    (2.0 * y /size_y) - 1.0)
             for x in range(size_x)]
            for y in range(size_y)]