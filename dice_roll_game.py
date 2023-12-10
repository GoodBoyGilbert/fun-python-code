import random

def diceRoll():
    
    print("Welcome to the dice roll game!")

    print("Here we will roll a random dice and if it matches your selection you win!")
    
    print("Pick a number bewteen 1 and 6: ")
    choice = int(input())

    if choice <= 0:
        print("That's not a number between 1 and 6 please try again")
        exit()

    if choice > 6:
        print("That's not a number between 1 and 6 please try again")
        exit()
        

    random_selection = int(random.randint(1,6))

    if choice == random_selection:
        print(f"Yay you had the same selection as the computer! Your selection: {choice} computers: {random_selection}")
    else:
        print(f"Your selection was: {choice} The computers: {random_selection}")

diceRoll()
