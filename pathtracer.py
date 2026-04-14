from tqdm import tqdm
import math

from rtweekend import *
import rtweekend as rt
from hittable import hittable, hit_record
from hittable_list import hittable_list
from sphere import sphere

def ray_color(r, world):
    rec = hit_record()
    if (world.hit(r, 0, rt.infinity, rec)):
        return 0.5 * (rec.normal + color(1, 1, 1))

    unit_direction = unit_vector(r.direction)
    a = 0.5*(unit_direction.y + 1.0)
    return (1.0 - a) * color(1.0, 1.0, 1.0) + a * color(0.5, 0.7, 1.0)

def main():

    # Image
    aspectRatio = 16.0/9.0
    imgWidth = 400

    imgHeight = int(imgWidth/aspectRatio)
    if imgHeight < 1:
        imgHeight = 1

    world = hittable_list()

    world.add(sphere(point3(0, 0, -1), 0.5))
    world.add(sphere(point3(0, -100.5, -1), 100))

    # Camera
    focalLength = 1.0
    viewportHeight = 2.0
    viewportWidth = viewportHeight * (float(imgWidth)/imgHeight)
    camera_center = point3(0, 0, 0)

    # Vectors across horizontal and vertical viewport edges
    viewport_u = Vec3(viewportWidth, 0, 0)
    viewport_v = Vec3(0, -viewportHeight, 0)

    # Horizontal and vertical deltas from pixel to pixel
    pixelDelta_u = viewport_u/imgWidth
    pixelDelta_v = viewport_v/imgHeight

    # Location of the upper left pixel
    
    """
        Starting from the camera center, we first move center of the 
        viewport by subtracting the focal length.
        Then we compute u and v by taking half the viewports
        Imagine it as viewing the center of the image and getting to top left
    """
    viewport_upper_left = (camera_center 
                           - Vec3(0, 0, focalLength) 
                           - viewport_u/2 
                           - viewport_v/2
                           )
    
    pixel00_loc = (viewport_upper_left
                   + 0.5 * (pixelDelta_u + pixelDelta_v)
                   )
    

    print("P3")
    print(imgWidth, imgHeight)
    print("255")

    for j in tqdm(range(imgHeight)):
        for i in (range(imgWidth)):
            pixel_center = pixel00_loc + (i * pixelDelta_u) + (j * pixelDelta_v)
            ray_direction = pixel_center - camera_center
            r = Ray(camera_center, ray_direction)

            pixel_color = ray_color(r, world)

            write_color(pixel_color)

if __name__ == "__main__":
    main()