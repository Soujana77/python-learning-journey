# 1. Write a program to print the multiplication table of a given number using a for loop.
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)