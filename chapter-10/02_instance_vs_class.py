class Employee:
    language = "Python" #this is a class attribute
    salary = 120000 #this is a class attribute

harry = Employee()
harry.language = "Java" # this is an instance attribute, it belongs to the object harry
print(harry.language) # this will print Java because instance attribute will override the class attribute

