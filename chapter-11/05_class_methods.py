class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    @classmethod
    def changeCompany(cls, new_company):
        cls.company = new_company


# Before change
e1 = Employee("Harry")
e2 = Employee("Rohan")

print(e1.company, e2.company)

# Changing class attribute using class method
Employee.changeCompany("Microsoft")

# After change
print(e1.company, e2.company)