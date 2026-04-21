from rtweekend import *
from hittable import Hit_record, Hittable
from tqdm import tqdm

class Camera:
    def __init__(self):
        self.aspect_ratio = 1.0
        self.image_width = 100
        self.samples_per_pixel = 10
        self.max_depth = 10

        self.image_height = None
        self.pixel_samples_scale = None
        self.center = None
        self.pixel00_loc = None
        self.pixel_delta_u = None
        self.pixel_delta_v = None

    def render(self, world):
        self.initialize()

        print("P3")
        print(self.image_width, self.image_height)
        print("255")

        for j in tqdm(range(self.image_height)):
            for i in (range(self.image_width)):
                pixel_color = color(0,0,0)
                for sample in range(self.samples_per_pixel):
                    r = self.get_ray(i, j)
                    pixel_color += self.ray_color(r, self.max_depth, world)

                write_color(self.pixel_samples_scale * pixel_color)

    def initialize(self):
        self.image_height = int(self.image_width/self.aspect_ratio)
        if self.image_height < 1:
            self.image_height = 1


        self.pixel_samples_scale = 1.0 / self.samples_per_pixel
        self.center = point3(0, 0, 0)

        # Camera
        focalLength = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * (float(self.image_width)/self.image_height)

        # Vectors across horizontal and vertical viewport edges
        viewport_u = Vec3(viewport_width, 0, 0)
        viewport_v = Vec3(0, -viewport_height, 0)

        # Horizontal and vertical deltas from pixel to pixel
        self.pixel_delta_u = viewport_u/self.image_width
        self.pixel_delta_v = viewport_v/self.image_height


        """
            Starting from the camera center, we first move center of the 
            viewport by subtracting the focal length.
            Then we compute u and v by taking half the viewports
            Imagine it as viewing the center of the image and getting to top left
        """
        viewport_upper_left = (self.center 
                            - Vec3(0, 0, focalLength) 
                            - viewport_u/2 
                            - viewport_v/2
                            )
        
        self.pixel00_loc = (viewport_upper_left
                    + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)
                    )

    def ray_color(self, r, depth, world):
        if depth <= 0:
            return color(0, 0, 0)
        
        rec = Hit_record()

        if (world.hit(r, Interval(0, infinity), rec)):
            direction = random_on_hemisphere(rec.normal)
            return 0.5 * self.ray_color(Ray(rec.p, direction), depth-1, world)

        unit_direction = unit_vector(r.direction)
        a = 0.5*(unit_direction.y + 1.0)
        return (1.0 - a) * color(1.0, 1.0, 1.0) + a * color(0.5, 0.7, 1.0)
    
    def get_ray(self, i, j):
        offset = self.sample_square()
        pixel_sample = (self.pixel00_loc
                        + ((i + offset.x) * self.pixel_delta_u)
                        + ((j + offset.y) * self.pixel_delta_v)
        )

        ray_origin = self.center
        ray_direction = pixel_sample - ray_origin
        
        return(Ray(ray_origin, ray_direction))

    def sample_square(self):
        return Vec3(random_double() - 0.5, random_double() - 0.5, 0)