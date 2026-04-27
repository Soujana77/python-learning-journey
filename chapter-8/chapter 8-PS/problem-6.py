# Q6. Write a python function which converts inches to cms.

def inches_to_cm(inches):
    return inches * 2.54

value = float(input("Enter inches: "))
print("In centimeters:", inches_to_cm(value))