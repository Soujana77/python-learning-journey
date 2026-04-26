#Example 1: Print all elements of a list
fruits = ["apple", "banana", "mango", "grape"]

i = 0  # start index

while i < len(fruits):
    print(fruits[i])   # access element using index
    i += 1             # move to next index

    #Example 2: Sum of elements in a list
    numbers = [10, 20, 30, 40]

i = 0
total = 0

while i < len(numbers):
    total += numbers[i]   # add each element
    i += 1

print("Sum:", total)

#Example 3: Find a specific element
names = ["Ram", "Shyam", "Harry", "Riya"]

search = input("Enter name to search: ")

i = 0
found = False

while i < len(names):
    if names[i] == search:
        found = True
        break             # stop loop if found
    i += 1

if found:
    print("Name found")
else:
    print("Name not found")

    #Example 4: Print even numbers from list
    nums = [1, 2, 3, 4, 5, 6]

i = 0

while i < len(nums):
    if nums[i] % 2 == 0:
        print(nums[i])   # print even numbers
    i += 1