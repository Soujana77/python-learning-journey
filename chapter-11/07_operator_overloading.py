class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n


a = Number(5)
b = Number(3)

print(a + b)   # calls __add__

#Example 2
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary


e1 = Employee(50000)
e2 = Employee(60000)

print(e1 + e2)