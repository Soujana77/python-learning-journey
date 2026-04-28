import random
'''
1 for snake 
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice:")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}
you = youDict [youstr]

#By now we have 2 numbers computer and you. We have to compare them and decide the winner.

print(f"computer chose {reverseDict[computer]}")
print(f"you chose {reverseDict[you]}")

if (computer == you):
    print("It's a tie!")

else:    
 if(computer == -1 and you == 1):
    print("You win")

 elif(computer ==-1 and you ==0):
    print("you lose")

 elif(computer == 1 and you == -1):
    print("you lose")

 elif(computer == 1 and you == 0):
    print("you win")

 elif(computer == 0 and you == -1):
    print("you lose")

 else:
    print("something went wrong")
''' found a logic bug in the above code. The logic is correct but we can simplify it using the following code:
if (computer - you )==-1 or (computer - you ) ==2:
    print("You lose")
else:
   print("You win")   
   '''