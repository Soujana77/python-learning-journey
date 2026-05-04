class Employee:
    company = "Google"   # fixed spelling

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

'''
class Programmer(Employee):
    company = "Google Cloud"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def language(self):
        print(f"The name is {self.name} and he is good with {self.language} language")'''
class Programmer(Employee):
   company = "Google Cloud"
   def showLanguage(self):
      print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)