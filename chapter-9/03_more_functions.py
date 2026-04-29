f = open("chapter-9/file.txt")
#First way to read the file is to read the whole file at once using read() method. It will return a string containing the whole content of the file.
'''
lines = f.readlines()
print(lines, type(lines))
'''
#Second way is to read the file line by line using readline() method. It will return a string containing the content of the line. When there are no more lines to read, it will return an empty string "".
'''line1 = f.readline()
print(line1, type(line1))
line2 = f.readline()
print(line2, type(line2))
line3 = f.readline()
print(line3, type(line3))
line4 = f.readline()
print(line4, type(line4))'''

#Third way is to read the file line by line using a while loop. We can use readline() method to read the file line by line until we reach the end of the file.
line = f.readline()
while(line != ""):
    print(line, end="")
    line = f.readline()


f.close()

# ============================================
# PYTHON FILE FUNCTIONS - ALL IN ONE PROGRAM
# ============================================

# --------------------------------------------
# 1. WRITE MODE ("w")
# Creates a new file or overwrites existing file
# --------------------------------------------

with open("sample.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Welcome to Python File Handling\n")

print("Data written successfully.\n")


# --------------------------------------------
# 2. READ MODE ("r")
# Reads the contents of the file
# --------------------------------------------

with open("sample.txt", "r") as f:
    
    # read entire file
    content = f.read()
    
    print("Reading full file using read():")
    print(content)

print()


# --------------------------------------------
# 3. readline()
# Reads one line at a time
# --------------------------------------------

with open("sample.txt", "r") as f:
    
    line1 = f.readline()
    line2 = f.readline()

    print("Using readline():")
    print(line1)
    print(line2)

print()


# --------------------------------------------
# 4. readlines()
# Reads all lines and stores in list
# --------------------------------------------

with open("sample.txt", "r") as f:
    
    lines = f.readlines()

    print("Using readlines():")
    print(lines)
    print("Type:", type(lines))

print()


# --------------------------------------------
# 5. APPEND MODE ("a")
# Adds data at end without deleting old content
# --------------------------------------------

with open("sample.txt", "a") as f:
    
    f.write("This line is added using append mode.\n")

print("Data appended successfully.\n")


# --------------------------------------------
# 6. READING UPDATED FILE
# --------------------------------------------

with open("sample.txt", "r") as f:
    
    print("Updated File Content:")
    print(f.read())

print()


# --------------------------------------------
# 7. tell()
# Gives current cursor position
# --------------------------------------------

with open("sample.txt", "r") as f:
    
    print("Cursor position before reading:", f.tell())

    f.read(5)

    print("Cursor position after reading 5 chars:", f.tell())

print()


# --------------------------------------------
# 8. seek()
# Moves cursor to specific position
# --------------------------------------------

with open("sample.txt", "r") as f:
    
    f.seek(0)   # move cursor to beginning

    print("After seek(0):")
    print(f.read(5))

print()


# --------------------------------------------
# 9. FILE PROPERTIES
# --------------------------------------------

with open("sample.txt", "r") as f:
    
    print("File Name:", f.name)
    print("File Mode:", f.mode)
    print("Is File Closed?", f.closed)

print()


# --------------------------------------------
# 10. CHECK FILE CLOSED
# --------------------------------------------

f = open("sample.txt", "r")
print("Before closing:", f.closed)

f.close()

print("After closing:", f.closed)