import random

guess = input("Please enter a number between 1 and 10: ")

computer_guess = random.randint(0,10)

print(" ")

print(f"Your guess: {guess}, the computer's guess:{computer_guess}")
  
