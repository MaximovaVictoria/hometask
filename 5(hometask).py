import json

a = []
while True:
    name = input('Введите название')
    mount = int(input('Введите цену'))
    if name == 'стоп':
        break
    dict = {'name': name, 'mount': mount}
    a.append(dict)
with open('dz.json', 'w', encoding='UTF-8') as file:
    b = json.dump(a, file)


