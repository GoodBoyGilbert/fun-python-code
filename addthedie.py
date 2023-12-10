# Here we add two die together

import random

def addDie():
    print("Here we will add two die together")

    start = str(input("Press Y to begin: "))

    if start == "Y":

        roll_one = int(random.randint(1,6))
        roll_two = int(random.randint(1,6))

        total = roll_one + roll_two

        print(f"Here is the total: {total}")
    else:
        print("")


addDie()