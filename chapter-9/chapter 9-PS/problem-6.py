# Question 6:
# Write a program to mine a log file and find out whether it contains 'python'.

with open("log.txt", "r") as f:
    content = f.read()

if "python" in content.lower():
    print("Python is present")
else:
    print("Python is not present")