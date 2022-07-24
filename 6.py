import json

with open('dz.json', 'r') as file:
    b = json.load(file)
    a = 0
    for i in b:
        a+=i['mount']
print(a)
