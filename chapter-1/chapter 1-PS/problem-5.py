#Label the program written in problem 4 with comments
import os

# Step 1: Get list of files in current directory
files = os.listdir()

# Step 2: Create a dictionary
# Key = index number
# Value = file name
file_dict = {}

for i in range(len(files)):
    file_dict[i] = files[i]

# Step 3: Print dictionary
print("Contents of dictionary:")
for key, value in file_dict.items():
    print(key, ":", value)