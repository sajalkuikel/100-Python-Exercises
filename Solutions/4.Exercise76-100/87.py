missed = ["Portugal", "Germany", "Spain"]
missed = [i + "\n" for i in missed]

with open("missing.txt", "r") as file:
    countries = file.readlines()
    updated = sorted(countries + missed)
    print(updated)
with open("countries_updated.txt", "w") as file:
    for i in updated:
        file.write(i)