from math import sqrt

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def coords(self):
        return (self.x, self.y, self.z)

a = Vector(1, 2, 3)
b = Vector(2, 9, -1)
c = Vector(-9, -17, 7)

# 1
print(abs(a))

print((a+b).coords())
print((a-b).coords())

# 1.1
print(((a+b+c).x/3, (a+b+c).y/3, (a+b+c).z/3))

# 1.2
l = [Vector(1, 2, 3), Vector(2, 9, -1), Vector(-9, -17, 7),  Vector(8, -7, 10),  Vector(0, 13, 9),  Vector(-7, -6, -10)]

m = 0

for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            a = abs(l[i] - l[j])
            b = abs(l[j] - l[k])
            c = abs(l[i] - l[k])

            p = (a + b + c) / 2

            s = sqrt(p*(p-a)*(p-b)*(p-c))

            m = max(m, s)

print(m)