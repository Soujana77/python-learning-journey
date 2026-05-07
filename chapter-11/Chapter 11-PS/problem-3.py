# 3. Create a class 'Employee' and add salary and increment properties to it.
# Write a method 'salaryAfterIncrement' using property decorator with a setter.

class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = value - self.salary


e = Employee(50000, 5000)

print("Salary after increment:", e.salaryAfterIncrement)

e.salaryAfterIncrement = 60000

print("New Increment:", e.increment)