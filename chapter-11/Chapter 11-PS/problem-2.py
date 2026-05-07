# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"2D Vector = {self.x}i + {self.y}j")


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"3D Vector = {self.x}i + {self.y}j + {self.z}k")


v = Vector3D(2, 3, 4)
v.show()