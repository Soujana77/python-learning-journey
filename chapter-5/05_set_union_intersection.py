# Set operations    
a = {1, 2, 3}
b = {3, 4, 5}
a.union(b)           # {1, 2, 3, 4, 5}
a.intersection(b)    # {3}
a.difference(b)      # {1, 2}
a.symmetric_difference(b)  # {1, 2, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b)) 
#this method is used to find the elements that are present in either set a or set b but not in both sets. It returns a new set that contains the elements that are present in either set a or set b but not in both sets. In this case, it will return {1, 2, 4, 5} because these are the elements that are present in either set a or set b but not in both sets.
