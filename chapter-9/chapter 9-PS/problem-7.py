# Question 7:
# Write a program to find out the line number where python is present from ques 6.

with open("log.txt", "r") as f:
    lines = f.readlines()

line_no = 1

for line in lines:
    if "python" in line.lower():
        print(f"Python found at line {line_no}")
    line_no += 1