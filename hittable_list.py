from hittable import hittable, hit_record

class hittable_list(hittable):
    def __init__(self):
        self.objects = []

    def clear(self):
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    

    def hit(self, r, ray_tmin, ray_tmax, rec: hit_record):
        temp_rec = hit_record()
        hit_anything = False
        closest_so_far = ray_tmax

        for object in self.objects:
            if object.hit(r, ray_tmin, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = self.copy_from(temp_rec)

        return hit_anything