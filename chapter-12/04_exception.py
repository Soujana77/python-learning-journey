# EXCEPTIONS IN PYTHON
#
# Exceptions are errors that occur during program execution.
# They can crash the program if not handled properly.
#
# Python uses:
# try
# except
# else
# finally
#
# to handle exceptions safely.


# ---------------------------------------------------
# 1. BASIC EXCEPTION HANDLING
# ---------------------------------------------------

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except:
    print("Something went wrong")


# ---------------------------------------------------
# 2. HANDLING SPECIFIC EXCEPTIONS
# ---------------------------------------------------

try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid number")


# ---------------------------------------------------
# 3. USING ELSE
# ---------------------------------------------------
#
# else runs only if no exception occurs
#

try:
    n = int(input("Enter a number: "))
    print("Square:", n * n)

except ValueError:
    print("Invalid input")

else:
    print("Program executed successfully")


# ---------------------------------------------------
# 4. USING FINALLY
# ---------------------------------------------------
#
# finally always executes
# whether exception occurs or not
#

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error occurred")

finally:
    print("Execution completed")


# ---------------------------------------------------
# 5. FILE HANDLING EXCEPTION
# ---------------------------------------------------

try:
    with open("demo.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("File does not exist")


# ---------------------------------------------------
# 6. CUSTOM EXCEPTION USING raise
# ---------------------------------------------------

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise ValueError("You are not eligible")

    print("You are eligible")

except ValueError as e:
    print(e)


# ---------------------------------------------------
# 7. USING 'as' KEYWORD
# ---------------------------------------------------

try:
    a = 10 / 0

except Exception as e:
    print("Error:", e)


# ---------------------------------------------------
# COMMON EXCEPTIONS
# ---------------------------------------------------
#
# ValueError
# -> wrong value type
#
# ZeroDivisionError
# -> division by zero
#
# FileNotFoundError
# -> file not found
#
# IndexError
# -> invalid list index
#
# KeyError
# -> invalid dictionary key
#
# TypeError
# -> wrong data type operation
#
#
# ---------------------------------------------------
# IMPORTANT POINTS
# ---------------------------------------------------
#
# 1. try -> risky code
# 2. except -> handles errors
# 3. else -> runs if no error
# 4. finally -> always runs
# 5. raise -> manually create exception
#