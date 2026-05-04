class Employee:
    def __init__(self, name):
        self.name = name
        print("Employee constructor called")


class Coder(Employee):
    def __init__(self, name, language):
        super().__init__(name)   # calling Employee constructor
        self.language = language
        print("Coder constructor called")


class Programmer(Coder):
    def __init__(self, name, language, salary):
        super().__init__(name, language)   # calling Coder constructor
        self.salary = salary
        print("Programmer constructor called")


# Creating object
p = Programmer("Harry", "Python", 130000)

print(p.name, p.language, p.salary)