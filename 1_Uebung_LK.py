# Aufgabe 1

import math

class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"VECTOR LEN {(self.len())}"
    
    def len(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
A = Vector3(2,5,8)
print(A)

#Aufgabe 2, Aufgabenstellung falsch verstanden

class WGS84Coord:
    def __init__(self, longitude=0, latitude=0):
        self.setCoord((longitude, latitude))

    def __str__(self):
        return f"KOORDINATEN: {self._longitude} long, {self._latitude} lat"

    def setCoord(self, new_coord):
        new_long, new_lat = new_coord
        if new_long < -180 or new_long > 180:
            raise ValueError("Ungültiger Wert, Wertebereich der Längengrade zwischen -180 und 180.")
        elif new_lat < -90 or new_lat > 90:
            raise ValueError("Ungültiger Wert, Wertebereich der Breitengrade zwischen -90 und 90.")
        self._longitude = new_long
        self._latitude = new_lat

    def getCoord(self):
        return self._longitude, self._latitude
    
    coord = property(getCoord, setCoord)

C = WGS84Coord(34, 123)
print(C)
C.coord = (40, -50)
print(C)

#Aufgabe 2, Lösung Christen

class WGS84Coord:
    def __init__(self, lng=0.0, lat=0.0):
        self._longitude = lng
        self._latitude = lat
    


a = WGS84Coord(7.324546, 47.4354322)
b = WGS84Coord(183.45, 95.34)

