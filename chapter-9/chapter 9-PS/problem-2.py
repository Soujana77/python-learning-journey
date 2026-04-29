# The game() function in a program lets a user play a game and returns the score as an integer you need to write a file high score TXT which is either blank or contains the previous high score you need to write a program to update the high score whoever the game() function breaks the high score
import random

def game():
    print("You are playing the game...")
    score = random.randint(1,62)
    #Fetch the hiscore from the file
    with open("/chapter 9-PS/hiscore.txt", "r") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score:{score}")
    if(score>hiscore ):
        print("Congratulations! You have the new high score!")
        with open("/chapter 9-PS/hiscore.txt", "w") as f:
            f.write(str(score))