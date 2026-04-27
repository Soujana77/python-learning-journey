#Program to Greet a User Using Functions
# Step 1: Define the function
def greet_user(name):
    # This function takes the user's name as input
    print("Hello,", name + "! Welcome!")

# Step 2: Take input from user
user_name = input("Enter your name: ")

# Step 3: Call the function
greet_user(user_name)