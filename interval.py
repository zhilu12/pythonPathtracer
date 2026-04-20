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
    
    def clamp(self, x):
        if (x < self.min): 
            return self.min
        if (x > self.max): 
            return self.max
        return x
    
Interval.empty = Interval()
Interval.universe = Interval(-math.inf, math.inf)