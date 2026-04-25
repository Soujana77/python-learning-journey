#if elif ifelse ladder
# This program checks the age of the user and categorizes them as a minor, adult, or senior citizen.
age = int(input("Enter your age:"))
if age < 0:
    print("Invalid age.")
elif age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
print("This line will always be printed.")


