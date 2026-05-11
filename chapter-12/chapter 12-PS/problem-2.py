# Question 2:
# Write a program to print third, fifth and seventh element
# from a list using enumerate function.

l = [10, 20, 30, 40, 50, 60, 70, 80]

for index, item in enumerate(l):

    if index == 2 or index == 4 or index == 6:
        print(item)