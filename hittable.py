from abc import ABC, abstractmethod
from ray import Ray

class hit_record:
    def __init__(self):
        self.p = None
        self.normal = None
        self.t = 0.0

class hittable: 
    @abstractmethod
    def hit(self, r, ray_tmin, ray_tmax, rec):
        pass