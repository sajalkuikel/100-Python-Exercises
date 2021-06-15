import json

with open("file1.json", "r+") as file:
    d = json.loads(file.read())
    d["owners"].append(dict(firstName="Sjl", lastNam="Kuikel"))
    d["owners"].append(dict(firstName="Sal", lastNam="Kuikel"))

    file.seek(0)
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()
