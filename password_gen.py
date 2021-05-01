import secrets, time, random,os # Modules needed for this program

# FUNCTIONS

def export_password():
    '''Exports the password generated to a txt file'''
    export_prompt = input("Would you like to export your password? y/n: ")
    if export_prompt.lower() == "y":
        with open('password.txt', 'w') as password_export:
            password_export.write(f"Hi {name.title()}, \nPassword: {password_generator}.\nLength: {len(password_generator)}.")
            time.sleep(2.5)
            print(f"Success!, Password exported to '{os.getcwd()}' as 'password.txt'.")
    else:
        print(f"Goodbye {name.title()}, Have a nice day.")
        time.sleep(3.0)


# MAIN PROGRAM STARTS HERE
print("Random Password Generator")
time.sleep(1.5)
print("Hi, please enter your Name below;")
time.sleep(0.5)
name = input("Name: ")
print(f"Welcome {name.title()}, this little program generates Random Password of any length.") # title() method to capitalize the first letter of the nam given
time.sleep(1.5)
print(f""" Help:
(1) Generate a Random Password up to a Maximum Length of 256 characters.
(2) Generate a Random Password with a Length specified by you, {name.title()}.""")
time.sleep(0.3)
print(f"So {name.title()}, what would it be: 1 or 2?")
time.sleep(1.0)

try:
    # for better error management
    user_choice = int(input("Enter 1 or 2: "))
    if user_choice == 2:    
        print("Please enter your required password length below")
        time.sleep(0.5)
        password_length = int(input("Password Length: "))
        password_generator = secrets.token_hex(password_length) # gen. the password
        print(f"Success {name.title()}, here is your password:\n{password_generator}")
        time.sleep(0.5)
        print(f"Password length is {len(password_generator)}, cool right?")
        if password_length == 0: # checks if password_length is literally = 0
            print("Please enter a number greater than 0")
        export_password()
    elif user_choice == 1:
        print("Generating Password ...")
        x = random.randint(1,128)
        password_length = x
        password_generator = secrets.token_hex(password_length) # gen. the password        
        time.sleep(2.0)
        print(f"Success! {name.title()}, here is your password:\n{password_generator}")
        time.sleep(0.5)
        print(f"Password length is {len(password_generator)}, cool right?")
        export_password()

        
except ValueError: # print the message below, if password_length is not an int
    print("Please enter only Whole Numbers e.g. 1")
    
