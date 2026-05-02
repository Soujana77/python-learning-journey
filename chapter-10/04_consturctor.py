class Employee:
    language = "Python"   # Class attribute
    salary = 120000       # Class attribute

    # Constructor
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    # Instance method
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # Static method
    @staticmethod
    def greet():
        print("Good Morning")


# Creating object
harry = Employee("Harry", 130000, "Java")

# Calling methods
harry.getInfo()
harry.greet()

# Printing attributes
print(harry.name, harry.language, harry.salary)