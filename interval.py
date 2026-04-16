import math
class Interval:
    empty = None
    universe = None

    def __init__(self, min=math.inf, max=-math.inf):
        self.min = min
        self.max = max

    def size(self):
        return self.max - self.min
    
    def contains(self, x):
        return self.min <= x <= self.max
    
    def surrounds(self, x):
        return self.min < x < self.max
    
Interval.empty = Interval()
Interval.universe = Interval(-math.inf, math.inf)