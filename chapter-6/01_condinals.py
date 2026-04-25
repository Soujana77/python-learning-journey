# This program checks if the user is an adult or not based on their age.
#if else statement is used to make a decision based on the condition provided. If the condition is true, the code block under if will be executed, otherwise the code block under else will be executed.
a = int(input("Enter your age:"))
if a >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
  
print("This line will always be printed.")

#elif statement is used to check multiple conditions. It allows you to check for additional conditions if the previous conditions are false.
b = int(input("Enter your age:"))
if b < 0:
    print("Invalid age.")
elif b < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
print("This line will always be printed.")

