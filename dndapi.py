import requests

tipo = "classes"

nome = "barbarian"

url = "https://www.dnd5eapi.co/api/"+tipo+"/"+nome

data = requests.get(url).json()

print(data)