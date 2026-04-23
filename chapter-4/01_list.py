friends = ["Apple", "Orange",5.5 , 345, False, "AKASH", "Rohan"]

print(friends)
print(friends[0])
print()
friends[0]="Garpes"#Unlike strings lists are mutable, it means that we can change the value of a list after it is created.
print(friends)
print(friends[0])
print(friends[1:3])#slicing the list from index 1 to 2 (3 is exclusive)
print(friends[1:])#slicing the list from index 1 to the end