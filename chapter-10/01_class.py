class Employee:
    language = "Python" #this is a class attribute
    salary = 120000 #this is a class attribute


sanvi = Employee()
sanvi.name = "Sanvi" # this is an instance attribute, it belongs to the object sanvi
print(sanvi.name, sanvi.language, sanvi.salary)

rohan = Employee()
rohan.name = "Rohan" # this is an instance attribute, it belongs to the object rohan
print(rohan.name, rohan.language, rohan.salary)

''' Here name is an attribute and salary and salary and language are class 
attributes are they directly belong to the class
'''
