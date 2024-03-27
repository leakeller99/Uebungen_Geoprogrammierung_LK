import math

class Vektor3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y}, {self.z})"
    
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vektor3(self.x + other, self.y + other, self.z + other)
        else:
            return Vektor3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return Vektor3(self.x - other, self.y - other, self.z - other)
        else:
            return Vektor3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vektor3(self.x * other, self.y * other, self.z * other)
        else:
            return Vektor3(self.x * other.x, self.y * other.y, self.z * other.z)

    __rmul__ = __mul__

    def cross(self, other):
        return Vektor3((self.y * other.z) - (self.z*other.y),
                       (self.z * other.x) - (self.x*other.z),
                       (self.x * other.y) - (self.y * other.x))
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def normalize(self):
        len = math.sqrt(self.x**2+self.y**2+self.z**2)
        if len == 0:
            return Vektor3(0,0,0)
        else:
            return Vektor3(self.x/len, self.y/len, self.z/len)


a = Vektor3(3,4,2)
b = Vektor3(2,1,0)

c = a * b # Komponentenweise Multiplikation
print(c)

d = a.dot(b) # Skalarprodukt
print(d)

e = a.cross(b) # Kreuzprodukt
print(e)

f = a.normalize()
print(f)