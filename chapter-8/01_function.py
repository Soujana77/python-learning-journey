# Basic Syntax
def function_name(parameters):
    # code block
    return value   # optional

#Simple Function (No Parameters)
# function definition
def greet():
    print("Hello, welcome!")   # this runs when function is called

# function call
greet()

#Function with Parameters
def greet(name):
    print("Hello", name)

greet("Soujanya")   # passing argument

#Function with Return Value
def add(a, b):
    result = a + b
    return result   # send result back

sum_value = add(5, 3)
print(sum_value)

#Multiple Parameters
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Riya", 20)

#Default Parameters
def greet(name="Guest"):
    print("Hello", name)

greet()          # uses default
greet("Harry")   # overrides default

#Keyword Arguments
def info(name, age):
    print(name, age)

info(age=20, name="Ram")  # order doesn’t matter

#Function with Loop (Real Use)
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)

#Function with Condition
def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(check_even(4))  # True
print(check_even(5))  # False

#Function Definition
def function_name(parameters):
    # code block

#Example: Function Definition
# defining a function
 def greet():
    print("Hello, welcome!")

#Function Calling (How to use a function)
function_name()

#Example:Funtion call
greet()   # calling the function

#Complete Example (Definition + Calling)
# Step 1: Define function
def greet():
    print("Hello, welcome!")

# Step 2: Call function
greet()