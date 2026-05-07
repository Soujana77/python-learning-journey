# 5. Write a class vector representing a vector of n dimensions.
# Overload '+' and '*' operator which calculates sum and dot product.

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __add__(self, other):
        result = []

        for i in range(len(self.vec)):
            result.append(self.vec[i] + other.vec[i])

        return Vector(result)

    def __mul__(self, other):
        dot = 0

        for i in range(len(self.vec)):
            dot += self.vec[i] * other.vec[i]

        return dot

    def __str__(self):
        return " + ".join([f"{self.vec[i]}a{i+1}" for i in range(len(self.vec))])

    def __len__(self):
        return len(self.vec)


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Vector Addition:")
print(v1 + v2)

print("Dot Product:")
print(v1 * v2)