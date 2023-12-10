
# Here we take a user's input and display it back to them

def yourProfile():
    
    first_name = input("What's your first name?: ")
    
    last_name = input("What's your last name?: ")
    
    age = input("What's your age?: ")
    
    job = input("What's your job?: ")

    profile = [first_name, last_name, age, job]

    print(f"Here is your profile: {profile}")

yourProfile()