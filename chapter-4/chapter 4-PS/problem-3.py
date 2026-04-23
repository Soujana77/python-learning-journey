#Check that a tuple cannot be changed in python. Try to change the value of a tuple and see what happens.
a =(1,2,5,6)
a[2]=3 #This will give an error because tuples are immutable, it means that we cannot change the value of a tuple after it is created. So, we cannot change the value of a tuple by assigning a new value to an index.
print(a)         
     
