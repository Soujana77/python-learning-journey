def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
         print(http_status(5007))

 # DICTIONARY MERGE AND UPDATE OPERATIONS IN PYTHON


# ---------------------------------------------------
# 1. MERGING DICTIONARIES USING |
# ---------------------------------------------------
#
# Combines two dictionaries into one
# Available in Python 3.9+
#

dict1 = {
    "name": "Harry",
    "age": 21
}

dict2 = {
    "city": "Delhi",
    "course": "Python"
}

merged = dict1 | dict2

print(merged)

# Output:
# {'name': 'Harry', 'age': 21, 'city': 'Delhi', 'course': 'Python'}


# ---------------------------------------------------
# 2. MERGING WITH SAME KEYS
# ---------------------------------------------------
#
# If keys are same, second dictionary value overrides first
#

d1 = {
    "name": "Harry",
    "age": 21
}

d2 = {
    "age": 25,
    "city": "Mumbai"
}

result = d1 | d2

print(result)

# Output:
# {'name': 'Harry', 'age': 25, 'city': 'Mumbai'}


# ---------------------------------------------------
# 3. UPDATE() METHOD
# ---------------------------------------------------
#
# update() modifies the original dictionary
#

student = {
    "name": "Rohan",
    "marks": 80
}

student.update({
    "marks": 95,
    "city": "Bangalore"
})

print(student)

# Output:
# {'name': 'Rohan', 'marks': 95, 'city': 'Bangalore'}


# ---------------------------------------------------
# 4. DIFFERENCE BETWEEN MERGE AND UPDATE
# ---------------------------------------------------
#
# | operator:
# -> creates NEW dictionary
#
# update():
# -> changes ORIGINAL dictionary
#


# ---------------------------------------------------
# 5. REAL-WORLD EXAMPLE
# ---------------------------------------------------

user_data = {
    "name": "Soujanya",
    "email": "soujanya@gmail.com"
}

new_data = {
    "phone": "9876543210",
    "city": "Bangalore"
}

# Merge user information
full_profile = user_data | new_data

print(full_profile)


# ---------------------------------------------------
# 6. UPDATE USING VARIABLES
# ---------------------------------------------------

employee = {
    "name": "Harry",
    "salary": 50000
}

employee.update(department="IT", location="Hyderabad")

print(employee)


# ---------------------------------------------------
# IMPORTANT POINTS
# ---------------------------------------------------
#
# 1. Dictionaries store key-value pairs
# 2. Keys must be unique
# 3. update() changes original dictionary
# 4. | operator creates a new dictionary
# 5. Duplicate keys get overwritten
#