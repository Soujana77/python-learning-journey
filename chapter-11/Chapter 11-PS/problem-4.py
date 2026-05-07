# 4. Write a class 'Complex' to represent complex numbers,
# along with overloaded operators '+' and '*'.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    def __mul__(self, other):
        real = (self.real * other.real) - (self.imag * other.imag)
        imag = (self.real * other.imag) + (self.imag * other.real)

        return Complex(real, imag)

    def show(self):
        print(f"{self.real} + {self.imag}i")


c1 = Complex(2, 3)
c2 = Complex(4, 5)

sumResult = c1 + c2
mulResult = c1 * c2

print("Addition:")
sumResult.show()

print("Multiplication:")
mulResult.show()