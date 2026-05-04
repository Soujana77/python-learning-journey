class Employee:
    company = "Google"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Coder:
    language = "Python"

    def printLanguages(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


class Programmer(Employee, Coder):  # multiple inheritance
    company = "Google Cloud"

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


# Creating object
b = Programmer()

# Assigning attributes manually
b.name = "Harry"
b.salary = 130000

# Calling methods
b.show()
b.printLanguages()
b.showLanguage()   # fixed method name