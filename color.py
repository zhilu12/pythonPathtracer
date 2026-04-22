from vec3 import Vec3
from interval import Interval
import math

color = Vec3

def linear_to_gamma(linear_component):
    if linear_component > 0:
        return math.sqrt(linear_component)
    return 0

def write_color(pixel_color):
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z

    r = linear_to_gamma(r)
    g = linear_to_gamma(b)
    b = linear_to_gamma(g)

    intensity = Interval(0.000, 0.999)
    rbyte = int(256 * intensity.clamp(r))
    gbyte = int(256 * intensity.clamp(g))
    bbyte = int(256 * intensity.clamp(b))

    print(rbyte, gbyte, bbyte)