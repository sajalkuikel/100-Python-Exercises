# Extract from json file and print them

import json
from pprint import pprint

with open ("file1.json", "r") as file:
    d= json.loads(file.read())
    pprint(d)
