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

#found a logic bug in the above code. The logic is correct but we can simplify it using the following code:
if (computer - you )==-1 or (computer - you ) ==2:
    print("You lose")
else:
   print("You win")   
   