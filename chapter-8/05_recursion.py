#Recursion (Advanced but important)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#Factorial calculation # Suppose n = 5

# factorial(5)
# = 5 * factorial(4)
# = 5 * (4 * factorial(3))
# = 5 * (4 * (3 * factorial(2)))
# = 5 * (4 * (3 * (2 * factorial(1))))
# = 5 * (4 * (3 * (2 * 1)))   # base case reached

# Now solving back:
# = 5 * (4 * (3 * 2))
# = 5 * (4 * 6)
# = 5 * 24
# = 120

# Function to calculate factorial using recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n * factorial(n-1)
    return n * factorial(n - 1)


# Taking input
num = int(input("Enter a number: "))

# Calling function
result = factorial(num)

print("Factorial is:", result)