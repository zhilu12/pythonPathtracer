from tqdm import tqdm
import math
from color import color
from color import write_color
from ray import Ray, Vec3, point3
from vec3 import unit_vector, dot

def ray_color(r):
    t = hit_sphere(point3(0, 0, -1), 0.5, r)
    if t > 0.0:
        N = unit_vector(r.at(t) - Vec3(0, 0, -1))
        return 0.5 * color(N.x + 1, N.y + 1, N.z + 1)
    
    
    
    unit_direction = unit_vector(r.direction)
    a = 0.5 * (unit_direction.y + 1.0)
    return (1.0 - a) * color(1.0, 1.0, 1.0) + a * color(0.5, 0.7, 1.0)

# creating a sphere in 3D space, if rays hit it, give the color red
def hit_sphere(center, radius, r):
    """ 
        (t^2 * d⋅d) - (2t * d⋅(C-Q)) + ((C-Q) ⋅ (C-Q) - r^2) = 0
            t = time t in which the ray intersects part of the sphere
            d = direction of the ray r
            C = center of the sphere
            Q = origin of the ray
            r = radius of sphere  
    """

    # vector from the ray to the center of the sphere
    oc = center - r.origin

    # using the quadrative formula to get values for a, b, c
    a = r.direction.length_squared()
    b = -2.0 * dot(r.direction, oc)
    c = oc.length_squared() - radius*radius


    # Subbing in b = -2h into the quadratic formula
    # = (h +- sqrt(h^2 - ac)) / a
    # and h = d * (C - Q)
    h = dot(r.direction, oc)

    # if discriminant is valid, that means there are possible values 
    # for t in which the ray intersects the sphere
    discriminant = h*h - a*c
    
    if discriminant < 0:
        return -1.0
    else:
        return ((h - math.sqrt(discriminant)) / a)



def main():

    # Image
    aspectRatio = 16.0/9.0
    imgWidth = 400

    imgHeight = int(imgWidth/aspectRatio)
    if imgHeight < 1:
        imgHeight = 1


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

            pixel_color = ray_color(r)

            write_color(pixel_color)

if __name__ == "__main__":
    main()