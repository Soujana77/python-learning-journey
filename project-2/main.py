'''Write a program that generates a random number
 and asks the user to guess it if a players
   guess is higher than the actual number the program displays lower number please
     similarly if the users guess is too low the program prints higher number please
       when the user cases the correct number the program displays the number of cases the
         player used to arrive at the number 
'''


import random 
a = int(input("Guess a number"))
n = random.randint(1,100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess a number"))
    if(a>n):
        print("Too high")   
        guesses = 1 + guesses
    elif(a<n):
        print("Too low")
        guesses = 1 + guesses
print(f"Congratulations! You guessed the number in {guesses} guesses")
