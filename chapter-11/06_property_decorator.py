class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary   # internal variable

    @property
    def salary(self):
        return self._salary


e = Employee("Harry", 50000)

print(e.salary)   # looks like attribute, but it's a method

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative")
        else:
            self._salary = value


e = Employee("Harry", 50000)

e.salary = 60000   # using setter
print(e.salary)