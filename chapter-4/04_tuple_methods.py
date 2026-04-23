d = ("Soujanya", 5.5, False, 345, "AKASH", "Rohan")
print(d)

no = d.count(5.5) #count() is a tuple method that returns the number of times a specified value appears in the tuple.
print(no) 

index = d.index("AKASH") #index() is a tuple method that returns the index of the first occurrence of a specified value in the tuple. If the value is not found, it raises a ValueError.
print(index)

i =d.index("AKASH", 3) #index() can also take two optional parameters, start and end, which specify the range of the tuple to search for the specified value. In this case, it will search for "AKASH" starting from index 3.   
print(i)

#tuple concatenation
t1 = (1,2,3)        
t2 = (4,5,6)
t3 = t1 + t2 #we can concatenate two tuples using the + operator,
print(t3)

print(len(d))#len() is a built-in function that returns the number of items in an object. In this case, it returns the number of items in the tuple d.

#Unpacking a tuple
a,b,c,d,e,f = d #we can unpack a tuple into individual variables, the number of variables must be equal to the number of items in the tuple.
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
    
