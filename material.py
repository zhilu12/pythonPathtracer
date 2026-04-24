from hittable import Material, Hit_record, ScatterRecord
from rtweekend import *

class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, r_in: Ray, rec: Hit_record, srec: ScatterRecord):
        scatter_direction = rec.normal + random_unit_vector()

        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        srec.scattered = Ray(rec.p, scatter_direction)
        srec.attenuation = self.albedo
        return True

class Metal(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, r_in: Ray, rec: Hit_record, srec: ScatterRecord):
        reflected = reflect(r_in.direction, rec.normal)
        srec.scattered = Ray(rec.p, reflected)
        srec.attenuation = self.albedo
        return True