s = { 1, 2 ,3, 4, 44, 55, 55, 55}
print(s)

s.add(66) #add() is a set method that adds an element to the set. If the element is already present in the set, it will not be added again because sets do not allow duplicate values.
print(s)
s.remove(44) #remove() is a set method that removes the specified element from the set. If the element is not present in the set, it will raise a KeyError.
print(s)    
s.discard(55) #discard() is a set method that removes the specified element from the set. If the element is not present in the set, it will not raise an error, it will simply do nothing.
print(s)    

s.pop()              # Removes a random element
print(s)
s.clear()            # Removes all elements
print(s)

a = {1, 2, 3}
b = {3, 4, 5}

# Set operations    
a.union(b)           # {1, 2, 3, 4, 5}
a.intersection(b)    # {3}
a.difference(b)      # {1, 2}
a.symmetric_difference(b)  # {1, 2, 4, 5}