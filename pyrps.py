from random import randint
import os
import time
import sys

t = ["rock", "paper", "scissors", "hackmii", "cheatcode"]
player = False

def ban_player():
    with open("rpsconf.ini", "w") as file:
        file.write("banwpsconfrpsrbxfps")

if os.path.exists("rpsconf.ini"):
    print("you have been banned from pyRPS for your actions.")
    sys.exit()

while player == False:
    computer = t[randint(0, 2)]
    player = input("rock, paper, scissors? ")
    if player == computer:
        print("tie!")
    elif player == "rock":
        if computer == "paper":
            print("you lose!")
        else:
            print("you win!")
    elif player == "paper":
        if computer == "scissors":
            print("you lose!")
        else:
            print("you win!")
    elif player == "scissors":
        if computer == "rock":
            print("you lose!")
        else:
            print("you win!")
    elif player == "hackmii":
        print("-hackmii mod activated-")
        print("you win!")
    elif player == "cheatcode":
        print("-cheatzone hack failed-")
        print("rebooting system...")
        time.sleep(2)
        print("-cheatzone hack failed-")
        ban_player()
        print("you have been banned from pyRPS for your actions.")
        
        
    else:
        print("this is not a valid move. check your spelling and try again.")