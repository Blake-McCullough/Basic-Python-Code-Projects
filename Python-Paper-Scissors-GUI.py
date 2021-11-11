#Made By Blake McCullough
#Discord- Spoiled_Kitten#4911
#Github- https://github.com/Blake-McCullough/




# Import Required Library
from tkinter import *
import random

# Create Object
root = Tk()

# Set geometry
root.geometry("300x300")

# Set title
root.title("Rock Paper Scissor Game")
#Choices available to play
choices = ["Rock", "Paper", "Scissors"]
#Sets variable to a string variable
winner = StringVar()
winner.set("------------------------")
#sets the label for saying CLICK AN OPTION
label = Label(root, text="Click on an option", relief=RAISED).pack()
#Sets label ready for variable
label = Label(root, textvariable=winner, relief=RAISED).pack()


def check_victory(computer_choice, user_choice):
    if user_choice == computer_choice:
      #Sets winner variable to show player tied and the computers choice 
        winner.set("You Tied! Computer Chose: " + computer_choice)

    elif computer_choice == "Rock" and user_choice == "Paper":
      #Sets winner variable to show player won and the computers choice 
        winner.set("You Win! Computer Chose: " + computer_choice)

    elif computer_choice == "Paper" and user_choice == "Scissors":
      #Sets winner variable to show player won and the computers choice 
        winner.set("You Win! Computer Chose: " + computer_choice)

    elif computer_choice == "Scissors" and user_choice == "Rock":
      #Sets winner variable to show player won and the computers choice 
        winner.set("You Win! Computer Chose: "+ computer_choice)

    else:
      #Sets winner variable to show player lost and the computers choice 
        winner.set("You  Lost! Computer Chose: " + computer_choice)


def play(user_choice):
    # get input from user
    user_choice = user_choice
    while user_choice not in choices:
        user_choice = user_choice

        # check if user wants to quit
        if user_choice == "Quit":
            sys.exit()
#Picks a random choice from dictionary of possible options
    computer_choice = random.choice(choices)

    #Run result result
    check_victory(computer_choice, user_choice)

#Creates buttons to show options
Button(root, text='Scissors', command=lambda *args: play("Scissors")).pack()
Button(root, text='Rock', command=lambda *args: play("Rock")).pack()
Button(root, text='Paper', command=lambda *args: play("Paper")).pack()
Button(root, text='Exit', command=lambda *args: play("Quit")).pack()
