checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_clean.txt", "r") as file:
    countries = file.readlines()
    countries = [i.strip("\n") for i in countries if "\n" in i]
    checked = [i for i in countries if i in checklist]
    print(checked)

