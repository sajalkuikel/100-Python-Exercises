from pip._vendor import requests

r = requests.get("http://www.pythonhow.com")
print(r.text[:100])