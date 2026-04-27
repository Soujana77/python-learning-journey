# Q1. Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    return max(a, b, c)   # built-in function

# input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Greatest number is:", greatest(x, y, z))