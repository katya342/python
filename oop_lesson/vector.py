class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return other.x + self.x, other.y + self.y,  other.z + self.z
    
    def __sub__(self, other):
        return other.x - self.x, other.y - self.y, other.z - self.z

if __name__ == "__main__":
   v1 = Vector(1, 2, 3)
   v2 = Vector(4, 5, 6)
   rezult_add = v1 + v2
   print(rezult_add)