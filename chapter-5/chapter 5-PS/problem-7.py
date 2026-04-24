# From previous problem if thee names of two friends are same : whtat will happen ?

d ={}       
name = input("Enter friends name:")
lang =  input("Enter language name:")
d.update({name:lang})

d ={}       
name = input("Enter friends name:")
lang =  input("Enter language name:")
d.update({name:lang})

d ={}       
name = input("Enter friends name:")
lang =  input("Enter language name:")
d.update({name:lang})

d ={}       
name = input("Enter friends name:")
lang =  input("Enter language name:")
d.update({name:lang})

print(d)
#If names of two friends are same then the value of the key will be updated with the new value. For example, if we have two friends named "Alice" and they both enter their favorite language, the dictionary will only store one entry for "Alice" and it will contain the favorite language of the second "Alice" that was entered. The first "Alice" entry will be overwritten by the second "Alice" entry. Therefore, we will lose the information about the first "Alice".
