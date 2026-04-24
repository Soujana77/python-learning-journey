marks = {
    "Sanvi": 95,
    "Rohan": 85,    
    "Akash": 90,
    "0" : "Harry"
}

print(marks.items())
#items() is a dictionary method that returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(marks.keys())
#keys() is a dictionary method that returns a view object that displays a list of all the keys in the dictionary.
print(marks.values())
#values() is a dictionary method that returns a view object that displays a list of all the values in the dictionary.
marks.update({"Rohan":99 , "Sanvi":70}) #update() is a dictionary method that updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs. If the key already exists in the dictionary, its value will be updated with the new value.
print(marks)    
marks.get("Rohan")#get() is a dictionary method that returns the value of the specified key. If the key does not exist in the dictionary, it returns None (or a specified default value).
print(marks.get("Rohan"))


