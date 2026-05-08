# WALRUS OPERATOR (:=) IN PYTHON
#
# Introduced in Python 3.8
#
# It is called the "Walrus Operator" because := looks a bit like walrus teeth 😄
#
# Purpose:
# It allows you to ASSIGN and USE a value in the same line.
#
# Syntax:
# variable := value
#
# Normal way:
# n = len(name)
# if n > 5:
#     print(n)
#
# Using walrus:
# if (n := len(name)) > 5:
#     print(n)
#
# This avoids writing the same thing multiple times.


# ---------------------------------------------------
# EXAMPLE 1: Checking length of a string
# ---------------------------------------------------

name = "Soujanya"

if (length := len(name)) > 5:
    print(f"Length is {length}")


# ---------------------------------------------------
# EXAMPLE 2: User input inside while loop
# ---------------------------------------------------
#
# Very useful in loops

while (text := input("Enter something: ")) != "quit":
    print("You entered:", text)


# ---------------------------------------------------
# EXAMPLE 3: Reading file content
# ---------------------------------------------------

with open("sample.txt", "r") as f:
    while (line := f.readline()) != "":
        print(line.strip())


# ---------------------------------------------------
# EXAMPLE 4: Working with lists
# ---------------------------------------------------

numbers = [10, 20, 30, 40]

if (total := sum(numbers)) > 50:
    print("Sum is:", total)


# ---------------------------------------------------
# EXAMPLE 5: Finding even numbers
# ---------------------------------------------------

nums = [1, 2, 3, 4, 5, 6]

even = [n for x in nums if (n := x % 2) == 0]

print(even)


# ---------------------------------------------------
# EXAMPLE 6: Game score example
# ---------------------------------------------------

score = 95

if (grade := score >= 90):
    print("Excellent")
    print("Condition value:", grade)


# ---------------------------------------------------
# KEY ADVANTAGES
# ---------------------------------------------------
#
# 1. Reduces repeated code
# 2. Makes loops cleaner
# 3. Useful in conditions
# 4. Helpful in file handling
#
# ---------------------------------------------------
# IMPORTANT NOTE
# ---------------------------------------------------
#
# Don't overuse walrus operator.
# Use it only when it improves readability.
#
# Too much walrus usage can make code confusing.