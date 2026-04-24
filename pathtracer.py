from tqdm import tqdm

from rtweekend import *
from material import Lambertian, Metal
from hittable_list import Hittable_list
from sphere import Sphere
from camera import Camera

def main():
    world = Hittable_list()

    material_ground = Lambertian(color(0.8, 0.8, 0.0))
    material_center = Lambertian(color(0.1, 0.2, 0.5))
    material_left = Metal(color(0.8, 0.8, 0.8))
    material_right = Metal(color(0.8, 0.6, 0.2))

    world.add(Sphere(point3( 0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(Sphere(point3( 0.0,    0.0, -1.2),   0.5, material_center))
    world.add(Sphere(point3(-1.0,    0.0, -1.0),   0.5, material_left))
    world.add(Sphere(point3( 1.0,    0.0, -1.0),   0.5, material_right))

    cam = Camera()
    cam.aspect_ratio = 16.0/9.0
    cam.image_width = 400
    cam.samples_per_pixel = 100
    cam.max_depth = 50

    cam.render(world)

if __name__ == "__main__":
    main()