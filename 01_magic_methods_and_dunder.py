class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)
    
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"
    
v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2
v4 = v1 - v2
v5 = v2 - v1
v6 = v1 * v2
v7 = v2 / v1
print(v3)
print(v4)
print(v5)
print(v6)
print(v7)