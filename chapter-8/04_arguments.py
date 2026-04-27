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