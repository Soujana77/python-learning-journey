#1. break in for loop
for i in range(1, 6):
    if i == 3:
        break   # stop loop when i is 3
    print(i)

#2. continue in for loop
for i in range(1, 6):
    if i == 3:
        continue   # skip 3
    print(i)

#3. Using break with list (real example)
names = ["Ram", "Shyam", "Harry", "Riya"]

for name in names:
    if name == "Harry":
        print("Found Harry!")
        break
    print(name)

#4. Using continue with condition
nums = [1, 2, 3, 4, 5]

for n in nums:
    if n % 2 == 0:
        continue   # skip even numbers
    print(n)

#5. Combined understanding
for i in range(1, 10):
    if i == 5:
        continue   # skip 5
    if i == 8:
        break      # stop at 8
    print(i)