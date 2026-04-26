# 10. Write a program to print the multiplication table of n using for loops in reversed order.
n = int(input("Enter a number: "))

for i in range(10, 0, -1):
    print(n, "x", i, "=", n * i)