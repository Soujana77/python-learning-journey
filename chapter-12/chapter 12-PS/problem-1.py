# Question 1:
# Write a program to open three files 1.txt, 2.txt and 3.txt.
# If any file is not present, print a message without exiting the program.

files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        with open(file, "r") as f:
            print(f.read())

    except FileNotFoundError:
        print(f"{file} is not present")