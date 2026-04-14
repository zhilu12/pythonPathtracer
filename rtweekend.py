import math
from vec3 import Vec3, point3, unit_vector, dot
from ray import Ray
from color import color, write_color

infinity = math.inf
pi = 3.1415926535897932385

def degrees_to_radians(degrees: float):
    return degrees * pi / 180.0