# Write a program to find whether a given user name contains less than 10 characters or not
user_name = input("Enter the user name: ")

if len(user_name) < 10:
    print("The user name contains less than 10 characters.")
else:
    print("The user name contains 10 or more characters.")