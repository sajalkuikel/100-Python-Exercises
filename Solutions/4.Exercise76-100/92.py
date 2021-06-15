import glob

file_list = glob.glob1("files.zip", "*.py")

print(len(file_list))