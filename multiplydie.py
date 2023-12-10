import random

#Here is a function that takes two random dice rolls and multiplies them

def dieRoll():
    first_roll = int(random.randint(1,6))
    
    second_roll = int(random.randint(1,6))

    print(f"Here is the first roll: {first_roll}")

    print(f"Here is the second roll: {second_roll}")

    total = f"{first_roll * second_roll}"

    print(f"Here is the die multiplied together: {total}")


dieRoll()