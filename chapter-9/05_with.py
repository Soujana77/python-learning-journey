f = open("file.txt")
print(f.read())
f.close()

#The same can be written using with statement like this :
with open("file.txt")as f:
    print(f.read())

#The with statement automatically takes care of closing the file after the block of code is executed, even if an error occurs. This makes it a safer and more convenient way to work with files in Python.