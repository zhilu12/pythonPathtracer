import math

class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.e = [x, y, z]

    @property
    def x(self):
        return self.e[0]
    
    @property
    def y(self):
        return self.e[1]
    
    @property
    def z(self):
        return self.e[2]
    
    def __repr__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"
    
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, other):
        if not isinstance(other, Vec3):
            raise TypeError("Can only add Vec3 to Vec3")
        return Vec3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
    
    def __sub__(self, other):
        if not isinstance(other, Vec3):
            raise TypeError("Can only subtract Vec3 to Vec3")
        return Vec3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vec3(self.x * other, 
                        self.y * other, 
                        self.z * other
            )
        
        elif isinstance(other, Vec3):
            return Vec3(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z
            )
        
        else: 
            raise TypeError("Unsupported operand type for *")
        
    def __rmul__(self, other):
        return self * other

    def __truediv__(self, t):
        return self * (1/t)
    
    def length(self):
        return math.sqrt(self.length_squared())
    
    def length_squared(self):
        return (
            self.x * self.x +
            self.y * self.y +
            self.z * self.z 
        )

point3 = Vec3

def dot(u, v):
    return (
        u.x * v.x 
        + u.y * v.y 
        + u.z * v.z
    )

def cross(u, v):
    return Vec3(
        u.e[1] * v.e[2] - u.e[2] * v.e[1],
        u.e[2] * v.e[0] - u.e[0] * v.e[2],
        u.e[0] * v.e[1] - u.e[1] * v.e[0]
    )

def unit_vector(u):
    return u / u.length()