# Password checker

while True:

    password = input("Enter the password: (MUST contain digit, Uppercase, and must be of 5 character or greater) ")
    if ( any(i.isdigit() for i in password) and any(i.isupper() for i in password) and len(password) >= 5):
        print("Thanks, Accepted!")
        break
    else:
        print("Please recheck your password and try again!")
