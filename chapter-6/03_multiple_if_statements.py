#Multiple if statements
age = 25
if age < 18:       
    print("You are a minor.")
if age >= 18 and age < 65:
    print("You are an adult.")
if age >= 65:
    print("You are a senior citizen.")
# In this example, we have three separate if statements to check the age of the user. Each if statement is evaluated independently, so all three conditions will be checked regardless of the previous conditions. This can lead to multiple outputs if the age falls into multiple categories. For example, if the age is 25, it will print "You are an adult." and "You are a senior citizen." because both conditions are true.

#Example 2
num = 15

if num > 0:
    print("Positive number")

if num % 3 == 0:
    print("Divisible by 3")

if num > 10:
    print("Greater than 10")