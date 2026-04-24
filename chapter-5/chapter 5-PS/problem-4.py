#what will be the length of the following set s 

s = set()
s.add(20)
s.add(20.0)
s.add('20') #Length os after these operations 
print(len(s)) #The length of the set s will be 2 because sets do not allow duplicate values. In this case, 20 and 20.0 are considered the same value because they are both equal to 20, so only one of them will be added to the set. The string '20' is a different value, so it will be added to the set as well. Therefore, the set will contain {20, '20'} and its length will be 2.