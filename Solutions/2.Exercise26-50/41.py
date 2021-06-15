import string

with open("letters.sql", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")