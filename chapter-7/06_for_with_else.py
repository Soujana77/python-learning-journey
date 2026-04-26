# Basic syntax

'''for item in sequence:
    # loop code
else:
    # runs if loop completes fully'''

#Example 1: Loop completes normally
for i in range(3):
    print(i)
else:
    print("Loop finished successfully")

   # Example 2: Loop stops using break
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished successfully")

  #  Example 3: Searching in a list (BEST use case)
names = ["Ram", "Shyam", "Harry"]

search = input("Enter name: ")

for name in names:
    if name == search:
        print("Found!")
        break
else:
    print("Not Found!")