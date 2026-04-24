# Can we have a set with 18(int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add('18')
print(s) #Yes, we can have a set with 18(int) and '18' (str) as a value in it because sets can contain elements of different data types. In this case, the set will contain the integer 18 and the string '18' as two distinct elements.