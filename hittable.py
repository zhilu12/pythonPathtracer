from abc import ABC, abstractmethod
from rtweekend import Ray, dot, Interval, color, random_unit_vector
 
class Hit_record:
    def __init__(self):
        self.p = None
        self.normal = None
        self.mat = None
        self.t = 0.0
        self.front_face = False

    def set_face_normal(self, r, outward_normal):
        self.front_face = dot(r.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

    # Helper method for copying record data
    def copy_from(self, other):
        self.p = other.p
        self.normal = other.normal
        self.mat = other.mat
        self.t = other.t
        self.front_face = other.front_face    

class Hittable(ABC): 
    @abstractmethod
    def hit(self, r: Ray, ray_t: Interval, rec: Hit_record):
        pass

class Material(ABC):
    @abstractmethod
    def scatter(self, r_in: Ray, rec: Hit_record, attenuation: color, scattered: Ray):
        pass

class Lambertian(Material):


    def scatter(self, r_in: Ray, rec: Hit_record, attenuation: color, scattered: Ray):
        scatter_direction = rec.normal + random_unit_vector()
        scattered = Ray(rec.p, scatter_direction)
        attenuation = albedo
        return True