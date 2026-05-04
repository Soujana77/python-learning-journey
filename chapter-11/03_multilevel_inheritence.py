class Employee:
    company = "Google"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Coder(Employee):   # inherits from Employee
    language = "Python"

    def printLanguages(self):
        print(f"The name is {self.name} and he is good with {self.language}")


class Programmer(Coder):   # inherits from Coder
    company = "Google Cloud"

    def showCompany(self):
        print(f"The name is {self.name} and works at {self.company}")


# Creating object
p = Programmer()

# Assigning attributes
p.name = "Harry"
p.salary = 130000

# Calling methods
p.show()             # from Employee
p.printLanguages()   # from Coder
p.showCompany()      # from Programmer