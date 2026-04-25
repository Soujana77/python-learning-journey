# Write a program which finds out whether a given name is present in in list or not

names = ["Soujj", "Sanvi", "Supriya", "David"]

search_name = input("Enter the name to search: ")

if search_name in names:
    print("Name is present in the list")
else:
    print("Name is NOT present in the list")