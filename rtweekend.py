import math
from vec3 import Vec3, point3, unit_vector, dot, random_on_hemisphere
from ray import Ray
from color import color, write_color
from interval import Interval
import numpy as np

infinity = math.inf
pi = 3.1415926535897932385

def degrees_to_radians(degrees: float):
    return degrees * pi / 180.0

def random_double(min=None, max=None):
    if (min and max):
        return np.random.uniform(min, max)
    return np.random.random()