import math
from hittable import Hittable, Hit_record, Material

from rtweekend import dot, Ray, Vec3, point3, Interval

class Sphere(Hittable):
    def __init__(self, center: point3, radius: float, mat: Material):
        self.center = center
        self.radius = max(0.0, radius)
        self.mat = mat

    def hit(self, r: Ray, ray_t, rec: Hit_record):
        # vector from the ray to the center of the sphere
        oc = self.center - r.origin

        # using the quadrative formula to get values for a, b, c
        a = r.direction.length_squared()
        h = dot(r.direction, oc)
        c = oc.length_squared() - self.radius*self.radius

        discriminant = h*h - a*c
        if discriminant < 0:
            return False
        
        sqrtd = math.sqrt(discriminant)

        root = (h - sqrtd) / a
        if (not ray_t.surrounds(root)):
            root = (h + sqrtd) / a
            if (not ray_t.surrounds(root)):
                return False
            
        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)
        rec.mat = self.mat

        return True