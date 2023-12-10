import random

while True:
    number_one = random.randint(0,100)
    number_two = random.randint(0,100)
    if number_one != number_two:
        print(f"{number_one} is not {number_two}")
        continue
    elif number_one == number_two:
        print(f"{number_one} is {number_two} Yay!")
        break

    