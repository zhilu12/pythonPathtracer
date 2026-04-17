from rtweekend import *
from hittable import Hit_record, Hittable
from tqdm import tqdm

class Camera:
    def __init__(self):
        self.aspect_ratio = 1.0
        self.image_width = 100

        self.image_height = None
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
                pixel_center = self.pixel00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
                ray_direction = pixel_center - self.center
                r = Ray(self.center, ray_direction)

                pixel_color = self.ray_color(r, world)

                write_color(pixel_color)

    def initialize(self):
        self.image_height = int(self.image_width/self.aspect_ratio)
        if self.image_height < 1:
            self.image_height = 1

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

    def ray_color(self, r, world):
        rec = Hit_record()
        if (world.hit(r, Interval(0, infinity), rec)):
            return 0.5 * (rec.normal + color(1, 1, 1))

        unit_direction = unit_vector(r.direction)
        a = 0.5*(unit_direction.y + 1.0)
        return (1.0 - a) * color(1.0, 1.0, 1.0) + a * color(0.5, 0.7, 1.0)