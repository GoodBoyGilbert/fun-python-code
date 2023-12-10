# Here this program will take your name and greet you

def theGreeting():
    first_name = input("Hello user, what is your first name?: ")
    last_name = input("What's your last name?: ")
    
    the_greeting = f"Hello {first_name} {last_name}, I hope you're having a great day!"

    print(the_greeting)

theGreeting()