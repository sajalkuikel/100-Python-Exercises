import string, os

if not os.path.exists("letters"):
    os.makedirs("letters")
for letters in string.ascii_uppercase:
    with open("letters/" +  letters + ".txt" ,"w") as file:
        file.write(letters + "\n")