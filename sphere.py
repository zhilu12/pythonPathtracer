import math
from hittable import hittable
from hittable import hit_record
from vec3 import dot
from ray import Ray, Vec3, point3  

class sphere(hittable):
    def __init__(self, center, radius):
        center = center
        radius = max(0.0, radius)

    def hit(self, r: Ray, ray_tmin, ray_tmax, rec: hit_record):
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
        if (root <= ray_tmin or ray_tmax <= root):
            root = (h + sqrtd) / a
            if (root <= ray_tmin or ray_tmax <= root):
                return False
            
        rec.t = root
        rec.p = r.at(rec.t)
        rec.normal = (rec.p - self.center) / self.radius

        return True
