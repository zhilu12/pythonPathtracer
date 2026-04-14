from abc import ABC, abstractmethod
from ray import Ray
from vec3 import dot

class hit_record:
    def __init__(self):
        self.p = None
        self.normal = None
        self.t = 0.0
        self.front_face = False

    def set_face_normal(self, r, outward_normal):
        self.front_face = dot(r.direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

    # Helper method for copying record data
    def copy_from(self, other):
        self.p = other.p
        self.normal = other.normal
        self.t = other.t
        self.front_face = other.front_face    

class hittable: 
    @abstractmethod
    def hit(self, r, ray_tmin, ray_tmax, rec):
        pass