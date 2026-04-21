#Write a program to calculate the square of a number entered by the user
a  = int(input("Enter value of a"))
print("Square of a is ", a*a)
print("Square of a is ", a**2) #using exponentiation operator to calculate square of a
print("Square of a is ", pow(a,2)) #using built in pow() function to calculate square of a
#a^2 is not a correct way to calculate square of a in python because ^ is a bitwise operator in python and it will not give the correct result for square of a