import random


def numberGame():
    print("Here we will multiply your input by 4 random numbers")
    num1 = int(input("Pick any number: "))
    num2 = int(input("Pick another number: "))

    total_number = int(random.randint(1, 9))
    print(f"First random number is: {total_number}")

    another_number = int(random.randint(1, 19))
    print(f"Second random number is: {another_number}")

    third_number = int(random.randint(1, 39))
    print(f"Third random number is: {third_number}")

    fourth_number = int(random.randint(1, 45))
    print(f"Fourth random number is: {fourth_number}")

    final_number = num1 * num2 * total_number * \
        another_number * third_number * fourth_number

    print(f"The final result is: {final_number}")


numberGame()
