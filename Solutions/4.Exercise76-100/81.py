# username and password
while True:
    usr = input("Enter your username : ")
    with open("users.txt", "r") as file:
        users = file.readlines()
        print(users)
        users = [i.strip("\n") for i in users]
    if usr in users:
        print("Username exists")
        continue
    else:
        print("Username is fine")
        break

while True:
    msg= []
    psw= input("Enter the password: ")

    if not any(i.isdigit() for i in psw):
        msg.append("You need at least one number! ")
    if not any(i.isupper() for i in psw):
        msg.append("You need at least one upper case character")
    if not len(psw) >= 5:
        msg.append("Password must be at least 5 characters long")
    if (len(msg)==0):
        print("Thanks, Accepted!")
        break
    else:
        print("Please check the following: ")
        for texts in msg:
            print(texts)
