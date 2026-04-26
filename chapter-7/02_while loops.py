# While loop
while condition:
    # code runs again and again 
    i = 1

#Example 1: Basic counting
while i <= 5:
    print(i)        # prints current value of i
    i += 1          # increase i by 1 (VERY IMPORTANT)


#Example 2: Sum of first n numbers
    n = int(input("Enter a number: "))
i = 1
total = 0

while i <= n:
    total += i      # add i to total
    i += 1          # move to next number

print("Sum is:", total)


#Example 3: User input until correct value
password = ""

while password != "admin123":
    password = input("Enter password: ")

print("Access Granted")


#Example 4: Infinite loop (with break)
while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break       # exits the loop
    
    print("You entered:", num)