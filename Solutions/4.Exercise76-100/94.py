import glob

with open("urls.txt", "r") as file:
    lines= file.readlines()
    print(lines)

with open("fixed.txt", "w") as file:
    for line in lines:
        line_remove = line.replace("s", "", 1)
        line_add_slash = line_remove[:6] + "/" + line_remove[6:]
        file.write(line_add_slash)