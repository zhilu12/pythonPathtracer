from hittable import Hit_record, Hittable, Interval

class Hittable_list(Hittable):
    def __init__(self):
        self.objects = []

    def clear(self):
        self.objects = []

    def add(self, object):
        self.objects.append(object)

    def hit(self, r, ray_t: Interval, rec: Hit_record):
        temp_rec = Hit_record()
        hit_anything = False
        closest_so_far = ray_t.max

        for object in self.objects:
            if object.hit(r, Interval(ray_t.min, closest_so_far), temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.copy_from(temp_rec)

        return hit_anything