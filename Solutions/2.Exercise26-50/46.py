import glob

letters = []

file_list = glob.glob("letters/*.txt")
# print(file_list)

for filename in file_list:
    with open(filename, 'r') as file:
        global letters_list
        letters_list = letters.append(file.read().strip("\n")) # strips cuts off everything from the file that is passed as the
                                                # argument

print(letters)

