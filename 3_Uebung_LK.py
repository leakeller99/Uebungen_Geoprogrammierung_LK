import math

class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"

class Figur:
    def __init__(self):
        self.name = "Figur"
    def Umfang(self):
        return 0
    def __str__(self):
        return self.name

class Dreieck(Figur):
    def __init__(self,a,b,c):
        super().__init__()
        self.name = "Dreieck"
        self.a = a
        self.b = b
        self.c = c
    
    def Umfang(self):
        AB = math.sqrt((self.b.x - self.a.x)**2 + (self.b.y - self.a.y)**2)
        BC = math.sqrt((self.c.x - self.b.x)**2 + (self.c.y - self.b.y)**2)
        CA = math.sqrt((self.a.x - self.c.x)**2 + (self.a.y - self.c.y)**2)
        return AB + BC + CA
    
    def __str__(self):
        return f"{self.name} A={self.a} B={self.b} C={self.c}"
    
class Rechteck(Figur):
    def __init__(self, a, b):
        super().__init__()
        self.name = "Rechteck"
        self.a = a
        self.b = b
    
    def Umfang(self):
        breite = abs(self.b.x - self.a.x)
        hoehe = abs(self.b.y - self.a.y)
        return 2 * (breite + hoehe)
    
    def __str__(self):
        return f"{self.name} ({self.a}) - ({self.b})"


class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__()
        self.name = "Kreis"
        self.M = mittelpunkt
        self.r = radius
    
    def Umfang(self):
        return 2 * math.pi * self.r
    
    def __str__(self):
        return f"{self.name} M={self.M} r={self.r}"


##class Polygon(Figur):
##    def __init__(self, punkte):
##        super().__init__("Polygon")
##       self.name = "Polygon"  --> keine Ahnung

p1 = Punkt(5, 3)
p2 = Punkt(3, 4)
p3 = Punkt(7,1)

d = Dreieck(p1, p2, p3)
r = Rechteck(p1, p2)
k = Kreis(p1, 5)

print(d, f"hat ein Umfang von: {d.Umfang()}")
print(r, f"hat ein Umfang von: {r.Umfang()}")
print(k, f"hat ein Umfang von: {k.Umfang()}")
