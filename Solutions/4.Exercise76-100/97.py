file = open("input_data_save.txt", "a+")

while True:
    inp = input("Enter the value: ")

    if inp == "SAVE":
        file.close()
        file = open("input_data_save.txt", "a+")
    elif inp == "CLOSE":
        file.close()
        break
    else:
        file.write(inp + "\n")



