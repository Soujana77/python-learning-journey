friends = ["Apple", "Orange",5.5 , 345, False, "AKASH", "Rohan"]

print(friends)

friends.append("Soujj")
print(friends)
friends.insert(1, "Mango")#inserts "Mango" at index 1
print(friends)
l1 = [1,34,45,67]
l1.sort()#sorts the list in ascending order
print(l1)
l1.reverse()#reverses the list
print(l1)
print(friends.pop(3))#removes the element at index 3 and returns it

l1.remove("AKASH")#removes the first occurrence of "AKASH" from the list
print(friends)