values = input("Enter the values: ")
values_list = values.split(",")

with open("values.txt", "a+") as file:
    for i in values_list:
        file.write(i + "\n")