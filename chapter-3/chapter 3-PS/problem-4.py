#Write a pprogram to detct double spaces in a string and replace them with single space.
name = "I am  Pushpa"
print(name.replace("  ", " "))#replace() is a string method that replaces a specified value with another value in a string.
print(name) #the original string is not changed because strings are immutable in python, it means that once a string is created, it cannot be changed. So, the replace() method returns a new string with the replaced value, but it does not change the original string.