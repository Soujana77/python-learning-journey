class Employee:
    language = "Python" #this is a class attribute
    salary = 120000 #this is a class attribute
   
    def getInfo(self): # self is a reference to the current object, it is used to access the attributes and methods of the class
        print(f"The language is {self.language}.  Employee class")
        print(f"The salary is {self.salary}.  Employee class")
    
    @staticmethod # this is a static method, it does not take self as a parameter, it can be called without creating an object of the class
    def greet():
        print("Good Morning")

harry = Employee()
harry.language = "Java" # this is an instance attribute, it belongs to the object harry
harry.getInfo() # this will print Java because instance attribute will override the class attribute
harry.greet() # this will print "Good Morning"