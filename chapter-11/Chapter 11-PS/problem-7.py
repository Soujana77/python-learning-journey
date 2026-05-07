# 7. Override the __len__() method on vector of problem 5
# to display the dimension of the vector.

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __len__(self):
        return len(self.vec)


v = Vector([1, 2, 3])

print("Dimension of vector:", len(v))