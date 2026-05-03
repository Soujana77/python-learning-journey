# Write a class "calculator" capable of finding square, cube and square root of a number
class Calculator:
    @staticmethod
    def square(num):
        return num ** 2
    
    @staticmethod
    def cube(num):
        return num ** 3
    
    @staticmethod
    def square_root(num):
        return num ** 0.5
    
    #Method-2
    class Calculator:
        def __init__(self, n):
            self.n = n

            def square(self):
                print(f"The square is {self.n*self.n}")
                def square(self):
                    print(f"The square is {self.n*self.n}")
                    def cube(self):
                        print(f"The cube is {self.n*self.n*self.n}")
                        def square_root(self):
                            print(f"The square root is {self.n**0.5}")

a = Calculator(4)
a.square()
                            