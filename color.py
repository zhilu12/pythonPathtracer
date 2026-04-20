from rtweekend import Vec3
from interval import Interval

color = Vec3

def write_color(pixel_color):
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z

    intensity = Interval(0.000, 0.999)
    rbyte = int(256 * intensity.clamp(r))
    gbyte = int(256 * intensity.clamp(g))
    bbyte = int(256 * intensity.clamp(b))

    print(rbyte, gbyte, bbyte)