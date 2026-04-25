# Write a program to calculate the grade of a student from his marks from the following scheme 90-200 excellent 80 to 90 A ,70 to 80 B ,60 to 70 C ,50 to 60 D ,less than 50 F

marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 200:
    print("Excellent")
elif marks >= 80 and marks < 90:
    print("Grade A")
elif marks >= 70 and marks < 80:
    print("Grade B")
elif marks >= 60 and marks < 70:
    print("Grade C")
elif marks >= 50 and marks < 60:
    print("Grade D")
elif marks < 50:
    print("Grade F")
else:
    print("Invalid marks")