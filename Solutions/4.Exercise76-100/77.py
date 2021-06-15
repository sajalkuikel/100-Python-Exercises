from datetime import datetime

age= int(input("Enter your age: "))

currentYear= int(datetime.now().strftime("%Y"))
dob = currentYear - age
print("We think you were born back in %s" %dob)