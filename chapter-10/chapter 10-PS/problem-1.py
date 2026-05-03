# Create a class Programmer with class attributes company and instance attributes name, salary and pincode. Create two objects of the class Programmer and print their attributes.
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Harry", 120000, 110092)
print(p.name,p.salary,p.pincode,p.company)
r = Programmer("Rohan", 150000, 110093)
print(r.name,r.salary,r.pincode,r.company)
