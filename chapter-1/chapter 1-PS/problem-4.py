# Write a python program to print the contents of a dictonary using the os module.
# Search online for the function which does that
import os
files = os.listdir()

file_dict = {}

for i in range(len(files)):
    file_dict[i] = files[i]

print("Contents of dictionary:")
for key, value in file_dict.items():
    print(key, ":", value)