
file = open("input_data.txt", "a+")

while True:
    inp = input("Enter a value: ")
    if inp == "CLOSE":
        file.close()
        break
    else:
        file.write(inp + "\n")

